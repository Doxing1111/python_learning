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


# open() 開啟檔案的語法
# open (檔案名稱[,模式][,編碼])
# 模式: r(讀取)、w(寫入, 若檔案已存在, 內容會被覆蓋)、a(附加模式, 若檔案已存在, 內容會被附加至尾端)

content = '''Hello Python!
Learning Python!
附加測試~
'''

f = open('test.txt', 'w', encoding='utf-8')
f.write(content)

content2 = 'TEST'
f = open('test.txt', 'a')
f.write(content2)

f = open('test.txt', 'r', encoding='utf-8') # 讀取以UTF-8編碼即可解決 'UnicodeDecodeError: 'cp950' codec can't decode byte 0xe8 in position 7: illegal multibyte sequence' 錯誤
for line in f:
    print(line, end="")
f.close() # 主動關閉


# 1 with 敘述結束後, 會自動關閉開啟的檔案
# 2 with 敘述內的程式必須縮排
with open('test.txt', 'r', encoding='utf-8') as f:
    for line in f:
        print(line, end="")


# read() 寫法一
f = open('test.txt', 'r', encoding='utf-8')
str1 = f.read(5)  # 讀取檔案的前5個字元, 如未輸入長度字元, 則讀取所有的字元
print(str1)
f.close()


# read() 寫法二
with open('test.txt', 'r', encoding='utf-8') as f:
    str1 = f.read(5)
    print(str1)




