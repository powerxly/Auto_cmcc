# -*- coding: utf-8 -*-
# __author__ = jason
# __date: 2019/5/14


import unittest
from selenium import webdriver
from Pages.ProductPage import ProductPage
from Base.BrowserDriver import BrowserDriver
from Func.login import login
import time
from selenium.webdriver.common.action_chains import ActionChains
class Test_inz_create_user(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        #driver = BrowserDriver(cls)
        #cls.driver = driver.openbrowser(cls)
        pass

    def setUp(self):
        pass

    def test_inz_create_org(self):
        driver = BrowserDriver(self)
        self.driver = driver.openbrowser(self)
        openresult = 0
        login.login(self.driver)
        pdt = ProductPage(self.driver)
        #点击应用管理
        pdt.click_app_manager()

        time.sleep(1)
        pdt.click_org_and_auth()
        time.sleep(1)
        pdt.click_user_manager()
        time.sleep(1)
        #

        time.sleep(1)
        #新建慧点科技下的用户
        for key,value in ProductPage.userListHD.items():
            self.driver.execute_script("$('#user_button > div.pull-right.btn-group > button:nth-child(1)').click()")
            self.driver.execute_script("$('#user_button > div.pull-right.btn-group > button:nth-child(1)').click()")
            self.driver.find_element_by_css_selector('#account').clear()
            self.driver.find_element_by_css_selector('#account').send_keys(key)
            self.driver.find_element_by_css_selector('#name').clear()
            self.driver.find_element_by_css_selector('#name').send_keys(value)
            pdt.click_o#content > ul > li:nth-child(3)rg_commit_button()
        time.sleep(1)
        #新建西安慧点科技下的用户
        for key,value in ProductPage.userListXAHD.items():
            self.driver.find_element_by_css_selector("#orgTree_2_switch").click()
            time.sleep()
            self.driver.find_element_by_link_text("西安慧点科技").click()
            time.sleep(1)
            # 点击新建用户
            self.driver.execute_script("$('#user_button > div.pull-right.btn-group > button:nth-child(1)').click()")
            time.sleep(1)
            self.driver.find_element_by_css_selector('#code').clear()
            self.driver.find_element_by_css_selector('#code').send_keys(key)
            self.driver.find_element_by_css_selector('#name').clear()
            self.driver.find_element_by_css_selector('#name').send_keys(value)
            pdt.click_org_commit_button()
        #新建北京慧点科技下的用户

        for key,value in ProductPage.userListBJHD.items():
            #加号展开
            #self.driver.find_element_by_css_selector("#orgTree_2_switch").click()
            time.sleep()
            self.driver.find_element_by_link_text("西安慧点科技").click()
            time.sleep(1)
            # 点击新建用户
            self.driver.execute_script("$('#user_button > div.pull-right.btn-group > button:nth-child(1)').click()")
            time.sleep(1)
            self.driver.find_element_by_css_selector('#code').clear()
            self.driver.find_element_by_css_selector('#code').send_keys(key)
            self.driver.find_element_by_css_selector('#name').clear()
            self.driver.find_element_by_css_selector('#name').send_keys(value)
            pdt.click_org_commit_button()




    @classmethod
    def tearDownClass(cls):
        pass

    def tearDown(self):
        pass

if __name__ == "__main__":
    unittest.main()