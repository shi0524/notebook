#! --*-- coding: utf-8 --*--

"""
选择排序
"""

from tools import time_it, random_list


# 版本一
@time_it
def insert_sort(arr):
    if not arr or len(arr) < 2:
        return
    N = len(arr)
    for i in range(N):
        """
        0 ~ 0   有序
        0 ~ 1   有序
        0 ~ 2   有序
        0 ~ 3   有序
        0 ~ i   有序
        """
        new_value_index = i
        for j in range(i-1, 0, -1):
            if arr[j] < arr[new_value_index]:
                break
            arr[j], arr[new_value_index] = arr[new_value_index], arr[j]
            new_value_index -= 1


# 版本二
@time_it
def insert_sort2(arr):
    if not arr or len(arr) < 2:
        return
    N = len(arr)
    for end in range(0, N):
        new_value_index = end
        while ((new_value_index - 1) > 0 and arr[new_value_index] < arr[new_value_index-1]):
            arr[new_value_index], arr[new_value_index-1] = arr[new_value_index-1], arr[new_value_index]
            new_value_index -= 1


# 版本三
@time_it
def insert_sort3(arr):
    """ 版本二的 无监督版
    """
    if not arr or len(arr) < 2:
        return
    N = len(arr)
    min_index = 0
    for _min in range(1, N):
        if arr[min_index] > arr[_min]:
            min_index = _min
    arr[0], arr[min_index] = arr[min_index], arr[0]

    for end in range(1, N):
        new_value_index = end
        while (arr[new_value_index] < arr[new_value_index-1]):
            arr[new_value_index], arr[new_value_index-1] = arr[new_value_index-1], arr[new_value_index]
            new_value_index -= 1


if __name__ == "__main__":
    arr = random_list(seed='algorithm')
    arr2 = arr[::]
    arr3 = arr[::]
    insert_sort(arr)        # 3953.08208466
    insert_sort2(arr2)      # 4547.58191109
    insert_sort3(arr3)      # 4005.49888611