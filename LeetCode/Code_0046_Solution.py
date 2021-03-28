#! --*-- coding: utf-8 --*--


"""
46. 全排列
给定一个 没有重复 数字的序列，返回其所有可能的全排列。

示例:

输入: [1,2,3]
输出:
    [
      [1,2,3],
      [1,3,2],
      [2,1,3],
      [2,3,1],
      [3,1,2],
      [3,2,1],
    ]
"""


class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = []
        ans = []
        self.process(nums, res, ans)
        return ans

    def process(self, nums, res, ans):
        if not nums:
            ans.append(res[::])
            return
        for i, j in enumerate(nums):
            res.append(j)
            self.process(nums[:i] + nums[i+1:], res, ans)
            res.pop()


if __name__ == "__main__":
    lst = [1, 2, 3]
    s = Solution()
    print s.permute(lst)
