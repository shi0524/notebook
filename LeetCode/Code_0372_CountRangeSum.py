#! --*-- coding: utf-8 --*--

"""
327. 区间和的个数

难度: 困难

给定一个整数数组 nums 。区间和 S(i, j) 表示在 nums 中，位置从 i 到 j 的元素之和，包含 i 和 j (i ≤ j)。
请你以下标 i （0 <= i <= nums.length ）为起点，元素个数逐次递增，计算子数组内的元素和。
当元素和落在范围 [lower, upper] （包含 lower 和 upper）之内时，记录子数组当前最末元素下标 j ，记作 有效 区间和 S(i, j) 。
求数组中，值位于范围 [lower, upper] （包含 lower 和 upper）之内的 有效 区间和的个数。

注意：
最直观的算法复杂度是 O(n2) ，请在此基础上优化你的算法。

示例：
输入：nums = [-2,5,-1], lower = -2, upper = 2,
输出：3
解释：
下标 i = 0 时，子数组 [-2]、[-2,5]、[-2,5,-1]，对应元素和分别为 -2、3、2 ；其中 -2 和 2 落在范围 [lower = -2, upper = 2] 之间，因此记录有效区间和 S(0,0)，S(0,2) 。
下标 i = 1 时，子数组 [5]、[5,-1] ，元素和 5、4 ；没有满足题意的有效区间和。
下标 i = 2 时，子数组 [-1] ，元素和 -1 ；记录有效区间和 S(2,2) 。
故，共有 3 个有效区间和。

提示：

0 <= nums.length <= 10^4

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/count-of-range-sum/

"""


class Solution(object):
    def countRangeSum(self, nums, lower, upper):
        """
        :type nums: List[int]
        :type lower: int
        :type upper: int
        :rtype: int
        """
        if not nums:
            return 0
        # 构建前缀和数组
        preSum = []
        preSum.append(nums[0])
        for i in nums[1:]:
            preSum.append(preSum[-1] + i)

        ans = self.process(preSum, 0, len(nums) - 1, lower, upper)

        return ans

    def process(self, preSum, L, R, lower, upper):
        if L == R:
            return 1 if lower <= preSum[L] <= upper else 0

        mid = (L + R) / 2

        return self.process(preSum, L, mid, lower, upper) \
               + self.process(preSum, mid + 1, R, lower, upper) \
               + self.merge(preSum, L, mid, R, lower, upper)

    def merge(self, preSum, L, M, R, lower, upper):
        ans = 0
        windowL = L
        windowR = L
        for i in preSum[M + 1: R + 1]:
            low = i - upper
            up = i - lower
            while windowL <= M and preSum[windowL] < low:
                windowL += 1
            while windowR <= M and preSum[windowR] <= up:
                windowR += 1
            ans += windowR - windowL

        p1 = L
        p2 = M + 1
        help = []
        while p1 <= M and p2 <= R:
            if preSum[p1] <= preSum[p2]:
                help.append(preSum[p1])
                p1 += 1
            else:
                help.append(preSum[p2])
                p2 += 1

        while p1 <= M:
            help.append(preSum[p1])
            p1 += 1
        while p2 <= R:
            p2 += 1

        for i, num in enumerate(help):
            preSum[L + i] = num

        return ans


if __name__ == "__main__":
    nums = [-2147483647, 0, -2147483647, 2147483647]
    lower = -564
    upper = 3864

    s = Solution()
    print s.countRangeSum(nums, lower, upper)
