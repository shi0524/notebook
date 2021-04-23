# -*- coding: utf-8 –*-

def largestDivisibleSubset(nums):
    """
    :type nums: List[int]
    :rtype: List[int]
    """
    nums.sort()
    n = len(nums)
    f = [0] * n
    g = [0] * n
    for i in range(n):
        # 至少包含自身，因此起始长度为1，由自身转移而来
        length, prev = 1, i
        for j in range(i):
            if nums[i] % nums[j] == 0:
                # 如果能接在更长的序列后面，则更新「最大长度」 &「从何转移而来」
                if f[j] + 1 > length:
                    length = f[j] + 1
                    prev = j
        # 记录「最终长度」& 「从何转移而来」
        f[i] = length
        g[i] = prev
    # 遍历所有长度 f[i], 取得「最大长度」 和 「对应下标」
    max_len = idx = -1
    for i in range(n):
        if f[i] > max_len:
            idx = i
            max_len = f[i]
    # 使用 g[] 数组回溯出具体方案
    ans = []
    while len(ans) < max_len:
        ans.append(nums[idx])
        idx = g[idx]
    ans.reverse()
    return ans


if __name__ == "__main__":
    l = [9, 18, 54, 90, 108, 180, 360, 540, 720]
    print largestDivisibleSubset(l)
