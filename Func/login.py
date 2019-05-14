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
class login():
    def login(browser):
        for key, value in ProductPage.userListAdmin.items():
            pdt = ProductPage(browser)
            pdt.input_pdt_username(key)
            pdt.input_pdt_password(value)
            pdt.click_pdt_btn()
            pdt.click_oa_link_button()
            pdt.change_to_right_window()


        time.sleep(1)


