'''
date: 2021/07/04
author: Joe
'''

# 使用 requests 讀取網頁原始碼
import requests

url = 'http://www.e-happy.com.tw/'
html = requests.get(url)
html.encoding = 'utf-8'
# print(html.text)
htmllist = html.text.splitlines()
for row in htmllist:
    print(row)