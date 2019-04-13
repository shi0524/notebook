# -*- coding: utf-8 –*-

import os
import json
import time
import datetime

#                 正文       title  addrs
SYS_MAIL_CMD = """echo '%s' | mail -s '%s' %s"""


def send_sys_mail(addr_list, subject, body):
    """
    send_sys_mail: 用系统名义给人发邮件
    args:
        addr_list: 发件人的list
        subject: 邮件标题
        body: 邮件正文
    returns:
        0    ---
    """
    addrs = ','.join(addr_list)

    cmd = SYS_MAIL_CMD%(body, subject, addrs)
    rc = os.system(cmd)
    return rc


def send_dingtalk(addr_url, subject, body):
    """
    发送到 钉钉
    """
    info = json.dumps({'text': {'content': '%s\n\n%s' % (subject, body)}, 'msgtype': 'text'})
    command = "curl %s -H 'Content-Type: application/json' -d '%s'" % (addr_url, info)
    os.system(command)


if __name__ == '__main__':

    mail_list = ['yufeng.shi@kaiqigu.com']
    dingtalk = 'https://oapi.dingtalk.com/robot/send?access_token=c5a3886c97dfaf2d9dfa2fd385b8b608f1a9f0fdfe35f6c84ed1014b1be10ed5'

    subject = '[mail test]'
    day = time.strftime('%Y-%m-%d %H:%M:%S')
    body = 'date: {}\n\n'.format(day)
    send_sys_mail(mail_list, subject, body)

    send_dingtalk(dingtalk, subject, body)