'''
date: 2021/07/13
author: Joe
'''


import unittest
from TestRunner import HTMLTestRunner
from time import sleep
from selenium import webdriver


class TestGoogle(unittest.TestCase):

    # 在每個測試類開始前先執行下方程式
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome()
        cls.base_url = 'https://google.com.tw'

    # 兩個測試案例步驟一樣, 將操作步驟封裝成一個方法
    def google_search(self, search_key):
        self.driver.get(self.base_url)
        self.driver.find_element_by_name('q').send_keys(search_key)
        sleep(2)
        self.driver.find_element_by_name('btnK').click()
        sleep(2)

    def test_search_key_unittest(self):
        search_key = 'unittest'
        self.google_search(search_key)
        self.assertEqual(self.driver.title, search_key + ' - Google 搜尋')

    def test_search_key_selenium(self):
        search_key = 'selenium'
        self.google_search(search_key)
        self.assertEqual(self.driver.title, search_key + ' - Google 搜尋')

    # 在每個測試類完成測試後執行下方程式
    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()


if __name__ == '__main__':
    suite = unittest.TestSuite()
    suite.addTest(TestGoogle('test_search_key_unittest'))
    suite.addTest(TestGoogle('test_search_key_selenium'))


    html_report = 'C:\\Users\\Li\\PycharmProjects\\python_learning\\m_unittest\\test_report\\test_report.html'
    fp = open(html_report, 'wb')
    runner = HTMLTestRunner(
        stream=fp,
        title='Test_Google by Selenium Test',
        description='For Joe Practice'
    )

    runner.run(suite)