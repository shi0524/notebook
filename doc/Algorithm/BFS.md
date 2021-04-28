# 宽度遍历

## 统计目录下所有的文件数量

```
给定一个文件目录的路径，
写一个函数统计这个目录下所有的文件数量并返回
隐藏文件也算，但是文件夹不算

思路:
    可以用树的递归遍历
    广度优先遍历即可

伪代码：
    ans = 0
    stack = []
    stack.add('A')
    while (!stack.empty()){
        X = stack.pop()
        files = 获取 X 里面的目录 和 文件
        for f in files：
            if f 是文件：
                ans += 1
            else:
                stack.add(f)
    }
        
讲解:
    大厂刷题班: 第1节 第2题 00:18:18
```

## 树中与target的距离是K的所有节点

```
给定三个参数：
二叉树的头节点head，树上某个节点target，正数K
从target开始，可以向上走或者向下走
返回与target的距离是K的所有节点

思路:
    先生成一个子节点与父节点的映射map, 这样便可由子节点反向找到父节点
    申请一个 记录遍历过的节点的集合 visited
    申请一个 队列 queue, 用于宽度优先遍历树的节点
    申请一个 层数 curLevel
    将 target 加入到 队列 queue 和 集合 visited 中
    批量处理：
        记录当前层 node 的数量 size
        如果 curlevel 不是目标 K
            则将当前层 size个 Node 的 父和子节点（不在visited中的），加入到queue, 同时将这size个节点加入到visited中
        如果 curlevel 是目标K
            收集这 size 个 Node 即为答案
            break 
        
讲解:
    大厂刷题班: 第3节 第8题 00:02:30
```