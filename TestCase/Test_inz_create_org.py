# -*- coding: utf-8 -*-
# __author__ = jason
# __date: 2019/5/13


import unittest
from selenium import webdriver
from Pages.ProductPage import ProductPage
from Base.BrowserDriver import BrowserDriver
from Func.login import login
import time
class Test_inz_create_org(unittest.TestCase):

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
        pdt.click_org_manager()
        time.sleep(2)
        #顶节点创建测试组织
        #self.driver.switch_to_frame('contentFrame')
        time.sleep(1)
        self.driver.execute_script("$('#contentDiv > div.table_btngroup.has_btnBar > div.pull-right.btn-group > button:nth-child(1)').click()")
        time.sleep(1)
        #新建慧点科技组织
        for key,value in ProductPage.orgListcodeHD.items():
            self.driver.find_element_by_css_selector('#code').clear()
            self.driver.find_element_by_css_selector('#code').send_keys(key)
            self.driver.find_element_by_css_selector('#name').clear()
            self.driver.find_element_by_css_selector('#name').send_keys(value)
            pdt.click_org_commit_button()
        #定位慧点科技，新建子公司
        time.sleep(1)

        for key,value in ProductPage.orgListcodeHDD.items():
            time.sleep(1)
            self.driver.find_element_by_link_text("慧点科技").click()
            time.sleep(1)
            self.driver.execute_script("$('#contentDiv > div.table_btngroup.has_btnBar > div.pull-right.btn-group > button:nth-child(1)').click()")
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