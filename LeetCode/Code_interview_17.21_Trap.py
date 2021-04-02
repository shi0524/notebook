#! --*-- coding: utf-8 --*--

"""
给定一个直方图(也称柱状图)，假设有人从上面源源不断地倒水，最后直方图能存多少水量?直方图的宽度为 1。

示例:
    输入: [0,1,0,2,1,0,1,3,2,1,2,1]
    输出: 6

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/volume-of-histogram-lcci
"""


class Solution(object):

    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        ans = 0
        N = len(height)
        if N < 3:
            return ans

        L = 1
        R = N - 2
        max_L = height[0]
        max_R = height[N - 1]
        while L <= R:
            if max_L < max_R:
                if height[L] < max_L:
                    ans += max_L - height[L]
                else:
                    max_L = height[L]
                L += 1
            else:
                if height[R] < max_R:
                    ans += max_R - height[R]
                else:
                    max_R = height[R]
                R -= 1
        return ans


if __name__ == "__main__":
    s = Solution()
    height = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
    print s.trap(height)
    height = [2, 0, 2]
    print s.trap(height)
