
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