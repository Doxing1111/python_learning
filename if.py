'''
date: 2021/05/30
author: Joe
'''

# break 強制跳出 ❮整個❯ 迴圈
for i in range(1, 10):
    if i == 6:
        break
    print(i, end= ',') # 1,2,3,4,5


# continue 強制跳出 ❮本次❯ 迴圈，繼續進入下一圈
for i in range(1, 10):
    if i == 6:
        continue
    print(i, end=',') # 1,2,3,4,5,7,8,9


# 樓層數跳過4不顯示
x = int(input('請輸入大樓樓層數: ')) # 輸入 10
print('本大樓樓層數共有: ')
if x > 3:
    x += 1 # x = 11
for i in range(1, x+1): # x+1= 12
    if i == 4:
        continue
    print(i, end=',') # 1,2,3,5,6,7,8,9,10,11


# while 迴圈 (通常用於沒有固定次數情況)
sum = n = 0
while n < 10:
    n += 1
    sum += n
    print(sum) # 查看加總變化 1,3,6,10,15,21,28,36,45,55
print(sum) # 1+2+3+4....+10=55
