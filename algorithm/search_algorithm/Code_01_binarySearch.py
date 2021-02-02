#! --*-- coding: utf-8 --*--


"""
二分查找
"""


def bin_earch(arr, num):
    """
    :param arr:     有序数组
    :param num:     要查找的数
    :return:        bool
    """
    if not arr:
        return False
    left = 0
    right = len(arr) - 1

    while (left <= right):
        middle = (left + right) / 2     # 其他语言会有整型超限问题, (python 没有)
        print middle, arr[middle]
        if arr[middle] == num:
            return True
        if arr[middle] < num:
            left = middle + 1
        else:
            right = middle - 1
    return False


if __name__ == "__main__":

    l = range(100)
    print bin_earch(l, 10)
