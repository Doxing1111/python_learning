'''
date: 2021/05/29
author: Joe
'''

# 串列 [List]
score = [60, 80, 95]
print('及格分數為: %d 分' % score[0])
print('甲等分數為: %d 分' % score[1])
print('優等分數為: %d 分' % score[2])

# 讀取串列元素
list1 = [0,1,2,3,4,5]
print(list1[0]) # [0]
print(list1[:5]) # [0, 1, 2, 3,4]
print(list1[1:]) # [1, 2, 3, 4, 5]
print(list1[2:4]) # [2, 3]
print(list1[:]) # [0, 1, 2, 3, 4, 5]
print(list1[-2:]) # [4, 5]
print(list1[:-3]) # [0, 1, 2]

# =========================================================================
# 運算式
top = float(input('請輸入梯形上底長度: '))
bottom = float(input('請輸入梯形下底長度: '))
height = float(input('請輸入梯形高度: '))
area = (top + bottom) * height / 2
print('梯形面積為: ' + str(area))

# ==========================================================================
# range 函式
# 串列變數 = range(起始值, 終止值-1, 間隔值)
list1 = range(1, 6, 1)
print(list(list1)) # [1, 2, 3, 4, 5]

list2 = range(-10, -5, 2)
print(list(list2)) # [-10, -8, -6]

# ==========================================================================
# for 迴圈
list1 = ['Apple', 'Orange', 'Banana']
for i in list1:
    print(i, end=', ') # Apple, Orange, Banana,

# ===========================================================================
sum = 0
x = int(input('請輸入正整數: ')) # 輸入 100
for i in range(1, x+1):
    sum += i
    print(sum) # 查看每次加總的變化
print('1 到 %d 的整數和為 %d' % (x, sum)) # 1 到 100 的整數和為 5050

# ============================================================================
# 巢狀 for 迴圈
# 九九乘法表
for i in range(1, 10):
    for j in range(1, 10):
        product = i * j
        print(product) # 查看每次加總的變化
        print('%d * %d = %2d    ' % (i, j, product), end='') # %2d 佔2個字元
    print()

# =============================================================================