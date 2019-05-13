#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Author  : Yagyi
# @Email   : 394856389@qq.com
import unittest
from selenium import webdriver
from Pages.ProductPage import ProductPage
from Base.BrowserDriver import BrowserDriver
import time
class Product_Case(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        #driver = BrowserDriver(cls)
        #cls.driver = driver.openbrowser(cls)
        pass

    def setUp(self):
        pass

    def test_donecheck(self):
        #打开浏览器
        self.driver = webdriver.Chrome()
        #访问uat
        self.driver.get('http://cloudoa.test.hq.cmcc/cmoa-webapp1/customlogin/login.jsp')
        #最大化窗口
        self.driver.maximize_window()
        #等待页面加载完成，30秒超时
        self.driver.implicitly_wait(30)
        self.driver.find_element_by_xpath('//*[@id="userName"]').send_keys('wangyimeng')
        self.driver.find_element_by_xpath('//*[@id="password"]').send_keys('Pa$$w0rd')
        self.driver.find_element_by_id('loginButton').click()
        time.sleep(2)
        self.driver.find_element_by_xpath('//*[@id="gViewCloseBtnGViewInfo"]').click()
        time.sleep(10)
        self.driver.switch_to.frame('iframecontent-utsmain')

        self.driver.find_element_by_xpath('/html/body/div[1]/div/div/div/div[1]/table/tbody/tr/td[2]/div/div/table/tbody/tr[1]/td[3]/a').click()
        time.sleep(20)


    @classmethod
    def tearDownClass(cls):
        pass

    def tearDown(self):
        pass

if __name__ == "__main__":
    unittest.main()