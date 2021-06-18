#! --*-- coding: utf-8 --*--

"""
异或的应用
"""

# 两个数交换 a, b (注意, a和b 必须有不同的内存地址)


def swap(a, b):
    a = a ^ b
    b = a ^ b
    a = a ^ b


# 找出一个数的最右边的为1的bit位
def find_rright_one(num):
    temp = ~num + 1
    return num & temp


# 一个正整数列表中, 一个出现了奇数次, 剩余出现偶数次, 找出奇数次的数
def find_one(lst):
    eor = 0
    for i in lst:
        eor ^= i
    return eor


# 两个出现了奇数次, 找出奇数
def find_two(lst):
    eor1 = 0
    for i in lst:
        eor1 ^= i
    right_one = eor1 & (~eor1 + 1)
    eor2 = 0
    for i in lst:
        if (i & right_one):
            eor2 ^= i

    return eor2, eor1^eor2


# 统计一个数字bit位为1的个数
def count_bit1(num):
    count = 0
    while num:
        count += 1
        right_one = num & (~num + 1)    # 取最右侧bit位为1其余位为0的数
        num ^= right_one                # 抹掉num最右bit位上的1
    return count


# 统计一个数字bit位为1的个数
def count_bit2(num):
    count = 0
    while num:
        count += 1
        num &= num - 1                  # 抹掉num最右bit位上的1  num & (num - 1)
    return count


