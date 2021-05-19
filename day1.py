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

# ============================================================
score = 95
print('喬得到的分數為: ' + str(score))

# ============================================================
a = b =c = 10
d = a + b
print(d) # 20

age, name = 29, "Mark"
print(name, age) # Mark 29

# ============================================================
# sep = 分隔字元, end = 結束字元
print('這件衣服的價格為', 1750,  sep = ": ", end = " $") # 這件衣服的價格為: 1750 $

# ============================================================
money = input("請輸入金額: ")
print(money)

# ============================================================
apple = int(input("請輸入蘋果價格: ")) # 20
banana = int(input("請輸入香蕉價格: ")) # 30
orange = int(input("請輸入橘子價格: ")) # 50
total = apple + banana + orange # 100
print("水果價格總額為： " + str(total)) # 水果價格總額為： 100

# ============================================================
