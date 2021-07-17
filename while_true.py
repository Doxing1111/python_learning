'''
date: 2021/07/17
author: Joe
'''

# x = 5
# while x < 10:
#     print('x小於10喔!')
#     print('迴圈中')
#     x = x + 1
#     print(x) # 查看值的變化
# print('跳出迴圈')

# ========================================

# while True:
#     mode = input('請輸入遊戲模式: ')
#     if mode == 'q':  # quit
#         break
#     elif mode == '1':
#         print('啟動模式一')
#     elif mode == '2':
#         print('啟動模式二')
#     else:
#         print('請輸入1或2或q')

# =========================================

''' 密碼重試程式
password = 'a123456'
讓使用者重複輸入密碼
最多輸入3次
如果正確就打印 "登入成功"
如果不正確就打印 "密碼錯誤! 還有__次機會!" 
'''

password = 'a123456'
i = 3 # 剩餘機會
while i > 0:
    i = i - 1
    pwd = input('請輸入密碼: ')
    if pwd == password:
        print('登入成功')
        break # 跳出迴圈
    else:
        print('密碼錯誤!')
        if i > 0:
            print('還有', i, '次機會')
        else:
            print('帳號已封鎖, 請洽客服')