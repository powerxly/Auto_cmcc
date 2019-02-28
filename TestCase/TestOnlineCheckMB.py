#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Author  : Yagyi
# @Email   : 394856389@qq.com

import unittest
from selenium import webdriver
from Pages.CmccPage import CmccPage
from Base.BrowserDriver import BrowserDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.touch_actions import TouchActions
import time
class TestOnlineCheckMB(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        # driver = BrowserDriver(cls)
        # cls.driver = driver.openbrowser(cls)
        pass

    def setUp(self):
        pass

    def test_todo(self):
        for key, value in CmccPage.userList.items():
            driver = BrowserDriver(self)
            self.driver = driver.openbrowsemobile(self)
            openresult = 0
            cmcc = CmccPage(self.driver)
            cmcc.input_cmcc_username_mb(key)
            cmcc.input_cmcc_password_mb(value)
            time.sleep(2)
            cmcc.click_cmcc_btn_mb()
            time.sleep(1)
            try:
                cmcc.click(CmccPage.firstTodomb)#这里入手，点击当前页面所有代办

                try:
                    cmcc.click(CmccPage.formText)  # 点击正文
                    cmcc.get_screent_img()
                except Exception as e:
                    print(Exception, ":", e)
                    print("没有正文")
                time.sleep(2)

                try:
                    cmcc.click(CmccPage.handleButton)  # 点击处理
                    cmcc.get_screent_img()
                except Exception as d:
                    print(Exception, ":", d)
                time.sleep(2)

            except Exception as c:
                print(Exception, ":", c)
                print("没有待办")
            time.sleep(2)

            self.driver.close()

    @classmethod
    def tearDownClass(cls):
        pass

    def tearDown(self):
        pass

if __name__ == "__main__":
    unittest.main()