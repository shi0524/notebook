# -*- coding: utf-8 –*-

import random


def swap(lyst, i, j):
    """ 交换列表中的 第i项 和 第j项
        lyst[i], lyst[j] = lyst[j], lyst[i]
    """
    temp = lyst[i]
    lyst[i] = lyst[j]
    lyst[j] = temp


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


if __name__ == "__main__":
    r = random.Random()
    lyst = range(10)

    print "*" * 50, "选择排序", "*" * 50
    r.seed('test_algorithm')
    r.shuffle(lyst)
    print lyst
    selection_sort(lyst)
    print lyst
    print "*" * 50, "选择排序", "*" * 50

    print "*" * 50, "冒泡排序", "*" * 50
    r.seed('test_algorithm')
    r.shuffle(lyst)
    print lyst
    bubble_sort(lyst)
    print lyst
    print "*" * 50, "冒泡排序", "*" * 50

    print "*" * 50, "插入排序", "*" * 50
    r.seed('test_algorithm')
    r.shuffle(lyst)
    print lyst
    insertion_sort(lyst)
    print lyst
    print "*" * 50, "插入排序", "*" * 50


