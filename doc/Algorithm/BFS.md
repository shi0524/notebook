

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