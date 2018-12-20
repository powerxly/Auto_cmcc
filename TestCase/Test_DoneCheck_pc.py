#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Author  : 洋燚
# @Email   : 394856389@qq.com

import unittest
from Pages.CmccPage import CmccPage
from Base.BrowserDriver import BrowserDriver
import time
class Test_DoneCheck_pc(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        pass

    def setUp(self):
        pass

    def test_donecheck(self):#啊啊
        for key,value in CmccPage.userList.items():
            driver = BrowserDriver(self)
            self.driver = driver.openbrowser(self)
            openresult = 0
            cmcc = CmccPage(self.driver)
            cmcc.input_cmcc_username(key)#改为列表读取
            cmcc.input_cmcc_password(value)
            cmcc.click_cmcc_btn()
            #cmcc.get_screent_img()
            cmcc.click(['id','gViewCloseBtnGViewInfo'])
            for i in range(5):
                try:
                    self.driver.switch_to.frame('iframecontent-utsmain')
                    cmcc.click(["xpath",'//*[@id="showRecord_2"]'])
                    cmcc.click(['xpath',("/html/body/div[1]/div/div/div/div[2]/table/tbody/tr/td[2]/div/div/table/tbody/tr[" + str(i+1) + "]/td[3]/a")])
                    time.sleep(3)
                    self.driver.implicitly_wait(30)

                    cmcc.change_to_window(1)
                    self.driver.implicitly_wait(30)
                    try:
                        cmcc.click(['id',"toFlowXspLink"])
                        #self.driver.find_element_by_id("processFormSubmitNext").click()
                        openresult = (i + 1)

                        cmcc.change_to_window(-1)
                        # windows = self.driver.window_handles
                        # self.driver.switch_to.window(windows[-1])
                        self.driver.close()

                        cmcc.change_to_window(-1)
                        # windows = self.driver.window_handles
                        # self.driver.switch_to.window(windows[-1])
                        self.driver.close()
                    except Exception as d:
                        print(Exception,":",d)
                        cmcc.get_screent_img()
                    #print("第" + str(i + 1) + "条已办打开正常")

                except Exception as e:
                    print(Exception,":",e)
                    print("没有第" + str(i + 1) + "条已办")
                    cmcc.get_screent_img()
                    break
                self.assertEqual(openresult, (i + 1), msg=("测试失败，第" + str(i + 1) + "条已办打开不正常"))
                cmcc.change_to_window(0)
            cmcc.close()

    @classmethod
    def tearDownClass(cls):
        pass

    def tearDown(self):
        pass


if __name__ == "__main__":
    unittest.main()