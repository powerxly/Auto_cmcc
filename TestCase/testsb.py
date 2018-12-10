#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Author  : Yagyi
# @Email   : 394856389@qq.com
import unittest
from selenium import webdriver
from Pages.CmccPage import CmccPage
from Base.BrowserDriver import BrowserDriver
import time
class CmccCase(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        #driver = BrowserDriver(cls)
        #cls.driver = driver.openbrowser(cls)
        pass

    def setUp(self):
        pass

    def test_donecheck(self):
        #打开浏览器
        driver = BrowserDriver(self)
        self.driver = driver.openbrowser(self)
        openresult = 0
        cmcc = CmccPage(self.driver)
        cmcc.input_cmcc_username('jianjie')
        cmcc.input_cmcc_password('Pa$$w0rd')
        cmcc.click_cmcc_btn()
        cmcc.click(['id','gViewCloseBtnGViewInfo'])
        cmcc.change_to_iframe('iframecontent-utsmain')
        cmcc.click(['xpath',"//*[@id='todo']/tbody/tr[1]/td[3]/a"])
        time.sleep(1)
        cmcc.change_to_window(1)
        time.sleep(4)
        cmcc.click(['id', "processFormSubmitNext"])
        self.driver.close()
        time.sleep(5)
        cmcc.change_to_window(0)
        cmcc.change_to_iframe('iframecontent-utsmain')
        cmcc.click(['xpath', "//*[@id='todo']/tbody/tr[1]/td[3]/a"])
        time.sleep(10)


    @classmethod
    def tearDownClass(cls):
        pass

    def tearDown(self):
        pass

if __name__ == "__main__":
    unittest.main()