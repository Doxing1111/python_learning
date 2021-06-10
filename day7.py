'''
date: 2021/06/11
author: Joe
'''

# os 模組 (提供建立目錄、刪除目錄、刪除檔案、執行作業系統命令等方法 (使用時必須匯入os模組)
# remove() 方法
import os

file = 'test.txt'

if os.path.exists(file):
    os.remove(file)
else:
    print(file + '　檔案尚未建立！')


# mkdir() 建立目錄方法
import os

dir = 'test'

if not os.path.exists(dir):
    os.mkdir(dir)
else:
    print(dir + ' 目錄已建立！')


# rmkdir() 刪除目錄方法
import os

dir = 'test'

if os.path.exists(dir):
    os.rmdir(dir)
else:
    print(dir + ' 目錄未建立！')


# system() 方法
import os
os.system('mkdir dir2') # 建立 dir2 目錄


# os.path 模組提供以下方法
# abspath 取得傳回檔案完整的路徑名稱
cur_path = os.path.abspath((__file__))
print(cur_path) # C:\Users\Li\PycharmProjects\python_learning\day7.py


# basename() 如果測試的是檔案會回傳檔名
cur_path = os.path.basename((__file__))
print(cur_path) # day7.py


# dirname() 取得目前的目錄路徑
cur_path = os.path.dirname((__file__))
print(cur_path) # C:/Users/Li/PycharmProjects/python_learning


# exists() 檢查檔案或路徑是否存在
cur_path = os.path.exists((__file__))
print(cur_path) # True


# split() 分割檔案目錄路徑、檔案名稱
cur_path = os.path.split((__file__))
print(cur_path) # ('C:/Users/Li/PycharmProjects/python_learning', 'day7.py')

