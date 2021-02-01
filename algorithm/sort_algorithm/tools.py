#! --*-- coding: utf-8 --*--

import time
import random


def time_it(func):
    """ 测时间 ms
    """
    def wrapper(*args, **kwargs):
        a = time.time()
        rc = func(*args, **kwargs)
        b = time.time()
        print (b - a) * 1000
        return rc
    return wrapper


def random_list(count=10000, max_value=10000, seed=None):
    """ 获取一个定长列表
    :param count:       列表总长度
    :param max_value:   随机最大值
    :param seed:        随机种子
    :return:
    """
    seed = seed or time.time()
    r = random.Random()
    r.seed(seed)
    lst = [r.randint(0, max_value) for _ in xrange(count)]
    return lst


def random_count_list(max_count=10000, max_value=10000, seed=None):
    """ 获取一个变长列表
    :param max_count:   列表总长度
    :param max_value:   随机最大值
    :param seed:        随机种子
    :return:
    """
    seed = seed or time.time()
    r = random.Random()
    r.seed(seed)
    count = r.randint(1, max_count)
    lst = [r.randint(0, max_value) for _ in xrange(count)]
    return lst


def check_is_sorted(lst):
    """ 检查 数组是否有序
    """
    if not lst:
        return True if lst == [] else False

    min_value = lst[0]

    N = len(lst)
    for i in range(1, N):
        if lst[i] < min_value:
            return False
        min_value = lst[i]
    return True