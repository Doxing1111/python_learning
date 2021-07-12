'''
date: 2021/07/13
author: Joe
'''

import unittest
from time import sleep
from selenium import webdriver


class TestGoogle(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.base_url = 'https://google.com.tw'

    def test_search_key_unittest(self):
        self.driver.get(self.base_url)
        sleep(2)
        self.driver.maximize_window()
        sleep(2)
        self.driver.find_element_by_name('q').send_keys('unittest')
        sleep(2)
        self.driver.find_element_by_name('btnK').click()
        sleep(2)
        title = self.driver.title
        self.assertEqual(title, 'unittest - Google 搜尋')

    def test_search_key_selenium(self):
        self.driver.get(self.base_url)
        sleep(2)
        self.driver.maximize_window()
        sleep(2)
        self.driver.find_element_by_name('q').send_keys('selenium')
        sleep(2)
        self.driver.find_element_by_name('btnK').click()
        sleep(2)
        title = self.driver.title
        self.assertEqual(title, 'selenium - Google 搜尋')

    def tearDown(self):
        self.driver.quit()


if __name__ == 'main':
    unittest.main()