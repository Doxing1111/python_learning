'''
date: 2021/07/17
author: Joe
'''

import requests
from bs4 import BeautifulSoup

html = requests.get('https://www.taiwanlottery.com.tw/result_all.htm')
html.encoding = 'utf-8'
sp = BeautifulSoup(html.text, 'html.parser')

data1 = sp.find('h1', class_='font_red18')
data2 = sp.find('table', class_='tableWin')
data3 = data2.find_all('span')
print(data1.text.strip()+'開獎順序:',end='')
for n in range(3, len(data3)):
    print(data3[n].text+' ', end='')

# ======================================================================
from bs4 import BeautifulSoup

myHtml=''''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>This is Crawler</title>
</head>
<body>
<h1>It's good a drink?</h1>
<h1>你喝喝看就知道了!</h1>
<h2>Who care?</h2>
<p>This is Joe, I'm 9527</p>
</body>
</html>'''

soup = BeautifulSoup(myHtml, 'html.parser')

myH1 = soup.find('h1')
# myH1 = soup.findAll('h1')

for i in myH1:
    if '你喝' in i.string:
        print(i.string)

    else:
        print('It s good a drink?')
    print(myH1) # <h1>It's good a drink?</h1>
    print(myH1.string) # It's good a drink?