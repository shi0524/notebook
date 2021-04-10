#! --*-- coding: utf-8 --*--

class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        N = len(nums)
        if N == 1:
            return nums[0]
        l = 0
        r = N - 1
        while l <= r:
            mid = (l + r) / 2
            if nums[mid] < nums[r]:
                r = mid
            elif nums[mid] > nums[r]:
                l = mid + 1
            else:
                r -= 1
        return nums[l]


if __name__ == "__main__":
    s = Solution()
    nums = [2, 2, 2, 0, 1]
    print s.findMin(nums)
