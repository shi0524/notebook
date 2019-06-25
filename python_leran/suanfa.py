# -*- coding: utf-8 –*-


def swap(lyst, i, j):
    """ 交换列表的i项和j项
    """
    lyst[i], lyst[j] = lyst[j], lyst[i]


def selection_sort(lyst):
    """ 选择排序
    原理 策略:
    搜索整个列表,找到最小项的位置, 如果该位置不是列表的第1个位置, 算法就会交换在这两个位置的项
    然后, 算法回到第二个位置, 并且重复这个过程
    """
    i = 0
    length = len(lyst)
    while i < length - 1:
        min_index = i
        j = i + 1
        while j < length:
            if lyst[j] < lyst[min_index]:
                min_index = j
            j += 1
        if i != min_index:
            swap(lyst, i, min_index)
        i += 1


def bubble_sort(lyst):
    """ 冒泡排序
    原理 策略
    从列表的开头处开始, 并且比较一对数据项, 直到移动到列表的末尾. 每当成对的两项之间的顺序不正确的时候,
    算法就会交换其位置. 这个过程的效果就是将最大项以冒泡的方式排到列表的末尾. 然后算法从列表开头的第2个
    列表项重复这个过程
    """
    length = len(lyst)

    while length > 1:
        i = 1
        while i < length:
            if lyst[i] < lyst[i-1]:
                swap(lyst, i, i-1)
            i += 1
        length -= 1


def bubble_sort2(lyst):
    """ 冒泡排序改良版
    """
    length = len(lyst)

    while length > 1:
        i = 1
        swapped = False
        while i < length:
            if lyst[i] < lyst[i-1]:
                swap(lyst, i, i-1)
                swapped = True
            i += 1
        if not swapped:
            break
        length -= 1


def insertion_sort(lyst):
    """ 插入排序
    在第i轮通过列表的时候(其中i的范围从1 到 n-1), 第i个项应该插入到列表的前i个项之中的正确位置
    在第i轮后, 前i个项应该是排好序的
    """
    i = 1
    length = len(lyst)
    while i < length:
        itemtoinsert = lyst[i]
        j = i - 1
        while j >= 0:
            if itemtoinsert < lyst[j]:
                lyst[j+1] = lyst[j]
                j -= 1
            else:
                break
        lyst[j+1] = itemtoinsert
        i += 1





