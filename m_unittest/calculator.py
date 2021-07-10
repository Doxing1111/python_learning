'''
date: 2021/07/10
author: Joe
'''


# 建立計算機類別
class Calculator:

    '''用於兩個數的加減乘除'''

    def __init__(self, a, b):
        self.a = int(a)
        self.b = int(b)

    def add(self):
        return self.a + self.b

    def sub(self):
        return self.a - self.b

    def mul(self):
        return self.a * self.b

    def div(self):
        return self.a / self.b

