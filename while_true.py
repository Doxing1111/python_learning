'''
date: 2021/07/17
author: Joe
'''

x = 5
while x < 10:
    print('x小於10喔!')
    print('迴圈中')
    x = x + 1
    print(x) # 查看值的變化
print('跳出迴圈')

# ========================================

while True:
    mode = input('請輸入遊戲模式: ')
    if mode == 'q':  # quit
        break
    elif mode == '1':
        print('啟動模式一')
    elif mode == '2':
        print('啟動模式二')
    else:
        print('請輸入1或2或q')