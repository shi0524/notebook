
# 动态规划

## 计算总的方法数

```
给定一个数组arr，你可以在每个数字之前决定+或者-
但是必须所有数字都参与
再给定一个数target，请问最后算出target的方法数是多少？

思路:
    暴力递归
        // 可以自由使用arr[index...]所有的数字 + 或 -
        // 搞出rest这个数, 方法数是多少
        process(int[] arr, int index, int rest)
    ↓
    记忆化搜索
        缓存结构：
            map = {
                indx1: {
                    reset1: num1,
                    reset2: num2,
                },
                indx2: {
                    reset1: num1,
                    reset2: num2,
                }
            }
        方法：
        process(int[] arr, int index, int reset, HashMap<Integer, HashMap<Integer, Integer>> map)
    ↓
    优化：
        1. 有负数, 全变成正数(根据题意, 不影响结果)
        2. 对非负数求和, 目标数 target > sum, 方法数为0, 不可能出现
        3. target 和 sum 奇偶性不一样, 0 中方法
        4. 把所有取正的数叫 P, 所有取负的数叫 N
           则有: P - N = target
                P-N + (P + N) = target + (P + N)
                2P = target + (P + N)
                2P = target + sum
                p = (target + sum)/2
           => 因为P确定, N 也就确定，故只要有一个正数集合是 (target + sum)/2, 就一定意味着有一种结果
           => 用 arr 凑 (target + sum)/2
              比如非负数组arr，target = 7, 而所有数累加和是11
	          求使用所有数字的情况下，多少方法最后形成7？
	          其实就是求有多少个子集的累加和是9 -> (7 + 11) / 2
           => 背包问题

        5. 二维动态规划空间压缩技巧
讲解:
    大厂刷题班: 第1节 第7题 01:00:00
```

## 司机调度问题
```
现有司机N*2人，调度中心会将所有司机平分给A、B两个区域
第 i 个司机去A可得收入为income[i][0]，
第 i 个司机去B可得收入为income[i][1]，
返回所有调度方案中能使所有司机总收入最高的方案，是多少钱

思路:
    因为是均分到两个区域, 故司机需为偶数
    去区域A 的司机确定, 去 区域B 的也会确定
    故可减少一个参数

伪代码:
    // index  ... 所有的司机, 往A和B区域分配
    // 返回把 index... 司机分配完，并且最终A和B区域一样多的情况下, index ... 这些司机的收益最大是多少
    process(int[] income, int index, int reset){
        N = income.length
        M = N >> 1
        // basecase1 去A区域的司机已经满了, 剩下的全部去B区域
        if (reset == 0){
            return income[index][1] + process(income, index + 1, reset)
        }
        // basecase2 剩余的司机全部都去A区域，才能均分司机
        if (N - index == reset){
            return income[index][0] + process(income, index + 1, reset-1)
        }
        
        // 普通情况
        pA = income[index][0] + process(income, index + 1, reset-1)
        pB = income[index][1] + process(income, index + 1, reset)
        
        return max(pA, pB);
    }

讲解:
    大厂刷题班: 第2节 第4题 02:05:30

```

## 最长无重复字符子串长度（leetcode 3）
```
求一个字符串中，最长无重复字符子串长度
https://leetcode.com/problems/longest-substring-without-repeating-characters/

思路:
    （这个问题, 窗口是可做的）
    子串、子数组问题 首先想到以i开头、以结尾
    
    以i位置字符结尾时, 子串的长度
    例:
        17 位置是 a, 则确定子串长度的 有两个因素
            1. 字符 a 上次出现的位置
            2. 以 16 位置结尾的子串的往左推的距离
    具体代码看 LeetCode
讲解:
    大厂刷题班: 第3节 第1题 00:45:23
```

## 自由之路
```
电子游戏“辐射4”中，任务“通向自由”要求玩家到达名为“Freedom Trail Ring”的金属表盘，并使用表盘拼写特定关键词才能开门。
给定一个字符串 ring，表示刻在外环上的编码；给定另一个字符串 key，表示需要拼写的关键词。您需要算出能够拼写关键词中所有字符的最少步数。
最初，ring 的第一个字符与12:00方向对齐。您需要顺时针或逆时针旋转 ring 以使 key 的一个字符在 12:00 方向对齐，然后按下中心按钮，以此逐个拼写完 key 中的所有字符。
旋转 ring 拼出 key 字符 key[i] 的阶段中：
您可以将 ring 顺时针或逆时针旋转一个位置，计为1步。旋转的最终目的是将字符串 ring 的一个字符与 12:00 方向对齐，并且这个字符必须等于字符 key[i] 。
如果字符 key[i] 已经对齐到12:00方向，您需要按下中心按钮进行拼写，这也将算作 1 步。按完之后，您可以开始拼写 key 的下一个字符（下一阶段）, 直至完成所有拼写。

链接：https://leetcode-cn.com/problems/freedom-trail

思路:
    
讲解:
    大厂刷题班: 第3节 第7题 02:10:00
```