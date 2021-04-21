
# 动态规划

## 


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