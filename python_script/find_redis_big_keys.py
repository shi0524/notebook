#! --*-- coding: utf-8 --*--

__author__ = 'shiyufeng'

"""
Redis提供了list、hash、zset等复杂类型的数据结构，
业务在使用的时候可能由于key设计不合理导致某个key过大，
由于redis简单的单线程模型，业务在获取或者删除大key的时候都会有一定的影响，
另外在集群模式下由于大key的产生还很容易导致某个子节点的内存满，综上所述我们需要提供大key的搜索工具。
"""

"""
对于Redis主从版本可以通过scan命令进行扫描，
对于集群版本提供了ISCAN命令进行扫描，
命令规则如下, 其中节点个数node可以通过info命令来获取到

ISCAN idx cursor [MATCH pattern] [COUNT count]（idx为节点的id，从0开始，16到64gb的集群实例为8个
"""

import sys
import redis


def check_big_key(r, k):
    bigKey = False
    length = 0
    try:
        type = r.type(k)
        if type == "string":
            length = r.strlen(k)
        elif type == "hash":
            length = r.hlen(k)
        elif type == "list":
            length = r.llen(k)
        elif type == "set":
            length = r.scard(k)
        elif type == "zset":
            length = r.zcard(k)
    except:
        return
    if length > 10240:
        bigKey = True
    if bigKey:
        print db, k, type, length


def find_big_key_normal(db_host, db_port, db_password, db_num):
    r = redis.StrictRedis(host=db_host, port=db_port, password=db_password, db=db_num)
    for k in r.scan_iter(count=1000):
        check_big_key(r, k)


def find_big_key_sharding(db_host, db_port, db_password, db_num, nodecount):
    r = redis.StrictRedis(host=db_host, port=db_port, password=db_password, db=db_num)
    cursor = 0
    for node in range(0, nodecount):
        while True:
            iscan = r.execute_command("iscan", str(node), str(cursor), "count", "1000")
            for k in iscan[1]:
                check_big_key(r, k)
            cursor = iscan[0]
            print cursor, db, node, len(iscan[1])
            if cursor == "0":
                break


if __name__ == '__main__':
    if len(sys.argv) != 4:
        print 'Usage: python ', sys.argv[0], ' host port password '
        exit(1)
    db_host = sys.argv[1]
    db_port = sys.argv[2]
    db_password = sys.argv[3]

    # db_host = '127.0.0.1'
    # db_port = 6900
    # db_password = ''

    r = redis.StrictRedis(host=db_host, port=int(db_port), password=db_password)
    nodecount = r.info().get('nodecount', 0)
    keyspace_info = r.info("keyspace")

    for db in keyspace_info:
        print 'check ', db, ' ', keyspace_info[db]
        if nodecount > 1:
            find_big_key_sharding(db_host, db_port, db_password, db.replace("db", ""), nodecount)
        else:
            find_big_key_normal(db_host, db_port, db_password, db.replace("db", ""))