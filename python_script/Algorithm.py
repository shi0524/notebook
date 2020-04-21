# -*- coding: utf-8 –*-

import time
import random


def time_it(func):

    def wrapper(*args, **kwargs):
        a = time.time()
        rc = func(*args, **kwargs)
        b = time.time()
        print (b - a) * 1000
        return rc
    return wrapper


def swap(lyst, i, j):
    """ 交换列表中的 第i项 和 第j项
        lyst[i], lyst[j] = lyst[j], lyst[i]
    """
    temp = lyst[i]
    lyst[i] = lyst[j]
    lyst[j] = temp

@time_it
def selection_sort(lyst):
    """ 选择排序
    """
    i = 0
    l = len(lyst)
    while i < l - 1:
        min_index = i
        j = i + 1
        while j < l:
            if lyst[j] < lyst[min_index]:
                min_index = j
            j += 1
        if min_index != i:
            swap(lyst, min_index, i)
        i += 1

@time_it
def bubble_sort(lyst):
    """ 冒泡排序
    """
    l = len(lyst)
    while l > 1:
        i = 1
        while i < l:
            if lyst[i] < lyst[i-1]:
                swap(lyst, i, i - 1)
            i += 1
        l -= 1

@time_it
def insertion_sort(lst):
    """ 插入排序
    """
    i = 1
    l = len(lyst)
    while i < l:
        item_to_insert = lyst[i]
        j = i - 1
        while j >= 0:
            if item_to_insert < lyst[j]:
                lyst[j + 1] = lyst[j]
                j -= 1
            else:
                break
        lyst[j + 1] = item_to_insert
        i += 1

def quick_sort(lst):
    """ 快排
    """
    if lst == []:
        return []
    first = lst[0]
    left = []
    right = []
    for l in lst[1:]:
        left.append(l) if l < first else right.append(l)
    return quick_sort(left) + [first] + quick_sort(right)


if __name__ == "__main__":
    r = random.Random()
    lyst = range(100000)

    print "*" * 50, "选择排序", "*" * 50
    r.seed('test_algorithm')
    r.shuffle(lyst)
    # print lyst
    selection_sort(lyst)
    # print lyst
    print "*" * 50, "选择排序", "*" * 50

    print "*" * 50, "冒泡排序", "*" * 50
    r.seed('test_algorithm')
    r.shuffle(lyst)
    # print lyst
    bubble_sort(lyst)
    # print lyst
    print "*" * 50, "冒泡排序", "*" * 50

    print "*" * 50, "插入排序", "*" * 50
    r.seed('test_algorithm')
    r.shuffle(lyst)
    # print lyst
    insertion_sort(lyst)
    # print lyst
    print "*" * 50, "插入排序", "*" * 50

    print "*" * 50, "快速排序", "*" * 50
    r.seed('test_algorithm')
    r.shuffle(lyst)
    # print lyst
    a = time.time()
    lyst = quick_sort(lyst)
    b = time.time()
    print (b - a) * 1000
    # print lyst
    print "*" * 50, "快速排序", "*" * 50



