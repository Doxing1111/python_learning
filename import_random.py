'''
date: 2021/07/17
author: Joe
'''

''' 產生一個隨機整數1~100
讓使用者重複輸入數字去猜
猜對的印出 "恭喜猜中了!"
猜錯的印出 告訴他比答案小或大'''

import random
start = input('請決定範圍數字開始值: ')
end = input('請決定隨機數字範圍結束值: ')
start = int(start)
end = int(end)

r = random.randint(start, end)
count = 0
while True:
    count += 1 # count = count + 1
    num = input('請猜數字: ')
    num = int(num)
    if num == r:
        print('恭喜猜中了!')
        print('這是你猜的第', count, '次')
        break
    elif num > r:
        print('比答案大')
    elif num < r:
        print('比答案小')
    print('這是你猜的第', count, '次')
