
# 数据结构设计

## 实现一个有setAall 方法的 Hashmap
```
实现一个有setAall 方法的 Hashmap
map = {1: 2, 5: 7, 10: 20}
setAall:
    map.get(1)  => 2
    map.get(5)  => 7
    map.setAll(100)
    map.get(1)  => 100
    map.get(2)  => 100
    map.set(30, 1)
    map.get(30) => 1

思路:
    每条 set 记录操作时间(次数)
    setAll 单独记录 时间 值
    每条 get 取出数据，去和 setAll 时间比较
        旧的返回 setAll 的值
        新的返回真实值

伪代码：
    class MyHashMap{
        time = 0        时间点
        setAllTime = -1 (或无穷大)
        setAllValue = 0
        map = {
                1: (2, 1),
                5: (7, 2),
                10: (20, 3),
            }
        
        setAll(v){
            time++;
            setAllValue = v
            setAllTime = time
        }
        get(k){
            v = map.get(k)
            return v[1] > setAllTime ? return v[0] : setAllValue
        }
        set(k, v){
            time++;
            map.set(k, (v, time))
        }
    }
        
讲解:
    大厂刷题班: 第2节 新加题 00:43:43
```

## 打印消息流
```
已知一个消息流会不断地吐出整数 1~N，
但不一定按照顺序依次吐出
如果上次打印的序号为i， 那么当i+1出现时
请打印 i+1 及其之后接收过的并且连续的所有数
直到1~N全部接收并打印完
请设计这种接收并打印的结构

思路:
    链表 + head池 + tail池 + 等待编号waitNum
    
    信息来了，将信息添加到 head池 和 tail池
    如果 head池 有上一个编号
        拼接到上一个编号的尾部
        删除 head池 中该消息编号
        删除 tail池 中上个消息编号
    如果 tail 池 有下一个编号
        拼接下一个编号
        删除 tail池 中该消息编号
        删除 head池 中下个消息编号
    
    如果当前消息编号是 等待编号waitNum
    打印数据,更新 waitNum,打印数据从 head池 和 tail池 移除

讲解:
    大厂刷题班: 第2节 第3题 00:54:30
```