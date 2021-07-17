'''
date: 2021/07/17
author: Joe
'''

from selenium import webdriver
from time import sleep

path = 'C:\\Users\\Li\\PycharmProjects\\python_learning\\m_unittest\\chromedriver.exe'

b = webdriver.Chrome(path)
b.get('https://google.com.tw')
sleep(1)
b.maximize_window()
sleep(1)
b.find_element_by_name('q').send_keys('python')
sleep(1)
b.find_element_by_name('btnK').click()
sleep(1)
b.quit()