#! --*-- coding: utf-8 --*--

"""
选择排序
"""

from tools import time_it, random_list


# 版本一
@time_it
def bubble_sort(arr):
    if not arr or len(arr) < 2:
        return
    N = len(arr)
    for i in range(N):
        """
        0 ~ N-1
        0 ~ N-2
        0 ~ N-i
        0 ~ end
        """
        for j in range(0, N-1-i):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]


if __name__ == "__main__":
    arr = random_list(seed='algorithm')
    print arr
    bubble_sort(arr)    # 5654.24990654
    print arr