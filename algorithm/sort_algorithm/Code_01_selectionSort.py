#! --*-- coding: utf-8 --*--

"""
选择排序
"""

from tools import time_it, random_list


# 版本一
@time_it
def select_sort(arr):
    if not arr or len(arr) < 2:
        return
    N = len(arr)
    for i in range(N):
        """
        0 ~ N-1 ->0
        1 ~ N-1 ->1
        2 ~ N-1 ->2
        i ~ N-1 ->i
        """
        min_value_index = i
        for j in range(i+1, N):
            if arr[j] < arr[min_value_index]:
                arr[j], arr[min_value_index] = arr[min_value_index], arr[j]


if __name__ == "__main__":
    arr = random_list(seed='algorithm')
    print arr
    select_sort(arr)    # 4243.86191368 ms
    print arr