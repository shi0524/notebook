# -*- coding: utf-8 –*-

from functools import wraps

""" 装饰器
    使用 wraps 效果对比
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


if __name__ == "__main__":
    print test_open(11)
    print test_open.func_name, test_open.func_doc
    print '*' * 20
    print test_open_2(22)
    print test_open_2.func_name, test_open_2.func_doc
