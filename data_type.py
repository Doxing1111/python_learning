'''
date: 2021/05/19
author: Joe
'''

# 整數 int
num1 = 20
print(type(num1))

# 浮點數 float
num2 = 0.5
print(type(num2))

# 布林值 bool
num3 = True
print(type(num3))

# 字串 str
num4 = "55"
print(type(num4))

# TypeError: unsupported operand type(s) for +: 'int' and 'str'
num5 = num1 + int(num4) # 將字串轉型為整數進行相加 75
print(num5)

num5 = str(num1) + num4 # 將整數轉型為字串進行相加 2055
print(num5)





