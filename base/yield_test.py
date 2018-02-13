# -*- coding: utf-8 -*-

"""
通过斐波那契的例子来练习yield的用法
https://www.ibm.com/developerworks/cn/opensource/os-cn-python-yield/
"""


def fab(max):
    '''
    从第一个打印到第max个
    :param max: 
    :return: 
    '''
    n, a, b = 0, 0, 1
    while n < max:
        print b
        a, b = b, a + b
        n = n + 1


def fab_1(max):
    '''
    将结果放在返回数组中,但是随着max越大返回数据占用的内存越大
    :param max: 
    :return: 
    '''
    n, a, b = 0, 0, 1
    L = []
    while n < max:
        L.append(b)
        a, b = b, a + b
        n = n + 1
    return L


class Fab(object):
    """
    用一个可迭代的类来存斐波那契数列的最后一个值
    """

    def __init__(self, max):
        self.max = max
        self.n, self.a, self.b = 0, 0, 1

    def __iter__(self):
        return self

    def next(self):
        if self.n < self.max:
            r = self.b
            self.a, self.b = self.b, self.a + self.b
            self.n = self.n + 1
            return r
        raise StopIteration()


def fab_2(max):
    '''
    使用yield效果同Fab class
    :param max: 
    :return: 
    '''
    n, a, b = 0, 0, 1
    while n < max:
        yield b
        a, b = b, a + b
        n = n + 1


def read_file(fpath):
    '''
    应用yield来读取文件
    :param fpath: 
    :return: 
    '''
    BLOCK_SIZE = 1024
    with open(fpath, 'rb') as f:
        while True:
            block = f.read(BLOCK_SIZE)
            if block:
                yield block
            else:
                return
