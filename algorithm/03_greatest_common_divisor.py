#! --*-- coding: utf-8 --*--


def gcd(num1, num2):
    """ 求两个整数的最大公约数 (greatest common divisor)
    :param num1:
    :param num2:
    :return:
    """
    return num1 if num2 == 0 else gcd(num2, num1 % num2)
