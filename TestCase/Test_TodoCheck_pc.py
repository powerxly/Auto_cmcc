#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Author  : 洋燚
# @Email   : 394856389@qq.com

import unittest
from Pages.CmccPage import CmccPage
from Base.BrowserDriver import BrowserDriver
import time
class Test_TodoCheck_pc(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        pass

    def setUp(self):
        pass

    def test_todocheck(self):
        for key,value in CmccPage.userList.items():
            driver = BrowserDriver(self)
            self.driver = driver.openbrowser(self)
            openresult = 0
            cmcc = CmccPage(self.driver)
            cmcc.input_cmcc_username(key)
            cmcc.input_cmcc_password(value)
            cmcc.click_cmcc_btn()
            #cmcc.get_screent_img()
            cmcc.click(['id','gViewCloseBtnGViewInfo'])


            for i in range(4):
                try:
                    self.driver.switch_to.frame('iframecontent-utsmain')
                    self.driver.find_element_by_xpath("//*[@id='todo']/tbody/tr["+ str(i+1) +"]/td[3]/a").click()
                    time.sleep(3)
                    self.driver.implicitly_wait(30)
                    cmcc.change_to_window(1)
                    try:
                        cmcc.click(['id',"processFormSubmitNext"])
                        #self.driver.find_element_by_id("processFormSubmitNext").click()
                        openresult = (i + 1)
                        #time.sleep(2)
                        self.driver.close()
                    except Exception as d:
                        print(Exception,":",d)
                    #print("第" + str(i + 1) + "条待办打开正常")

                except Exception as e:
                    print(Exception,":",e)
                    print("没有第" + str(i + 1) + "条待办")
                    cmcc.get_screent_img()
                    break
                self.assertEqual(openresult, (i + 1), msg=("测试失败，第" + str(i + 1) + "条待办打开不正常"))
                cmcc.change_to_window(0)
            cmcc.close()

    @classmethod
    def tearDownClass(cls):
        pass

    def tearDown(self):
        pass


if __name__ == "__main__":
    unittest.main()