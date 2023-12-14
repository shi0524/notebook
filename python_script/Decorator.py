# -*- coding: utf-8 –*-

import random
from functools import wraps, partial

""" 装饰器
    使用 wraps 效果对比
    多层装饰器 与 偏函数
"""


def is_open(func):
    """ 有没有开启
    """
    def wrapper(*args, **kwargs):
        """ 装饰函数
        """
        pass
        return func(*args, **kwargs)
    return wrapper


@is_open
def test_open(lv):
    """ 测试开启
    """
    if lv > 10:
        return True
    return False


def is_open_2(func):
    """ 有没有开启
    """
    @wraps(func)
    def wrapper(*args, **kwargs):
        """ 装饰函数
        """
        pass
        return func(*args, **kwargs)
    return wrapper


@is_open_2
def test_open_2(lv):
    """ 测试开启
    """
    if lv > 10:
        return True
    return False


def test_rateA(rate):
    """ 测试概率A
    """
    def wrapper(func):
        """ 装饰函数A1
        """
        @wraps(func)
        def inner(*args, **kwargs):
            """ 装饰函数A2
            """
            if random.randint(1, 100) < rate:
                result = func(*args, **kwargs)
                return result
            return None  # 返回 None 或其他默认值
        return inner
    return wrapper


@test_rateA(50)
def test_rate_1(lv):
    """ 测试多层装饰器 传入概率
    """
    return range(lv)


def test_rateB(func, rate):
    """ 测试概率B
    """
    @wraps(func)
    def wrapper(*args, **kwargs):
        """ 装饰器函数B1
        """
        if random.randint(1, 100) < rate:
            result = func(*args, **kwargs)
            return result
        return None  # 返回 None 或其他默认值
    return wrapper


@partial(test_rateB, rate=50)
def test_rate_2(lv):
    """ 测试偏函数 传入概率
    """
    return range(lv)


if __name__ == "__main__":
    print test_open(11)
    print test_open.func_name, test_open.func_doc
    print '*' * 20
    print test_open_2(22)
    print test_open_2.func_name, test_open_2.func_doc

    print '=' * 20
    print test_rate_1(5)
    print test_rate_1(6)
    print test_rate_1.func_name, test_rate_1.func_doc


    print '=' * 20
    print test_rate_2(5)
    print test_rate_2(6)
    print test_rate_2.func_name, test_rate_2.func_doc

