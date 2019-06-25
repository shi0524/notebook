# -*- coding: utf-8 –*-

import inspect


def foo():
    who = inspect.getframeinfo(inspect.currentframe().f_back)[2]
    who1 = inspect.getframeinfo(inspect.currentframe(2))
    print '{} call me'.format(who), 1
    print '{} call me'.format(who1.function), 2

def a():
    foo()


def b():
    foo()

# a()
# b()
a()