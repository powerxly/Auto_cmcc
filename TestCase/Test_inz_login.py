# -*- coding: utf-8 -*-
# __author__ = jason
# __date: 2019/4/29

#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Author  : Yagyi
# @Email   : 394856389@qq.com
import unittest
from selenium import webdriver
from Pages.ProductPage import ProductPage
from Base.BrowserDriver import BrowserDriver
import time
class test_inz_login(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        #driver = BrowserDriver(cls)
        #cls.driver = driver.openbrowser(cls)
        pass

    def setUp(self):
        pass

    def test_inz_login(self):
        driver = BrowserDriver(self)
        self.driver = driver.openbrowser(self)
        openresult = 0
        for key, value in ProductPage.userList.items():
            pdt = ProductPage(self.driver)
            pdt.input_pdt_username(key)
            pdt.input_pdt_password(value)
            pdt.click_pdt_btn()
            pdt.click_oa_link_button()
            windows = self.driver.window_handles
            self.driver.switch_to.window(windows[1])


        #time.sleep(20)


    @classmethod
    def tearDownClass(cls):
        pass

    def tearDown(self):
        pass

if __name__ == "__main__":
    unittest.main()