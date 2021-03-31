#! --*-- coding: utf-8 --*--


"""
90. 子集 II

给你一个整数数组 nums ，其中可能包含重复元素，请你返回该数组所有可能的子集（幂集）。
解集 不能 包含重复的子集。返回的解集中，子集可以按 任意顺序 排列。

示例 1：
输入：nums = [1,2,2]
输出：[[],[1],[1,2],[1,2,2],[2],[2,2]]
示例 2：

输入：nums = [0]
输出：[[],[0]]

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/subsets-ii/
"""


class Solution01(object):
    """ 过程中去重
    """
    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        path = []
        ans = []
        self.dfs(nums, 0, path, ans)
        return ans

    def dfs(self, nums, index, path, ans):
        ans.append(path[:])
        for i in range(index, len(nums)):
            if index != i and nums[i] == nums[i-1]:
                continue
            path.append(nums[i])
            self.dfs(nums, i + 1, path, ans)
            path.pop()


class Solution02(object):
    """ 使用 set 去重
    """

    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        ans = set()
        cur = []
        self.dfs(nums, 0, cur, ans)
        return [list(x) for x in ans]

    def dfs(self, nums, u, cur, ans):
        if u == len(nums):
            ans.add(tuple(cur))
            return
        cur.append(nums[u])
        self.dfs(nums, u + 1, cur, ans)
        cur.pop()
        self.dfs(nums, u + 1, cur, ans)


if __name__ == "__main__":

    s1 = Solution01()
    s2 = Solution02()

    nums = [2, 1, 2, 3]
    print sorted(s1.subsetsWithDup(nums))
    print sorted(s2.subsetsWithDup(nums))
