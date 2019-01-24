# -*- coding: utf-8 -*-
# # # __author__ = 'duanhan'

# 完成bmhq（部门会签）脚本后再运行此脚本
#本脚本仅运行至发送文件，目的是仅测试多人任务环节是否正常
#查看待阅直接使用已有脚本

import unittest
from Pages.CmccPage import CmccPage
from Base.BrowserDriver import BrowserDriver
import time
import os.path
import yaml
from selenium.webdriver.common.action_chains import ActionChains

class Test_Gsfw_drqb(unittest.TestCase):


    @classmethod
    def setUpClass(cls):
        #driver = BrowserDriver(cls)
        #cls.driver = driver.openbrowser(cls)
        pass

    def setUp(self):
        pass

    def test_gsfw(self):
        #读取配置文件

        file_path = os.path.dirname(os.getcwd())
        name_path = file_path + '\yaml\\browser.yaml'
        with open(name_path, 'r') as f:
            temp = yaml.load(f.read())

        #读取xpath

        #提交按钮
        commit_xpath = temp['jcyj']['commit']
        #决策意见，同意单选框
        agree_xpath = temp['jcyj']['agree']
        #提交前人员确认框，确认按钮
        confirm_xpath = temp['confirm']
        #提交下一处理按钮
        next_xpath = temp['next']
        #普通意见，意见输入框
        text_xpath = temp['ptyj']['textarea']


        for key,value in CmccPage.userList_drqb.items():
            driver = BrowserDriver(self)
            self.driver = driver.openbrowser(self)
            self.driver.implicitly_wait(30)
            cmcc = CmccPage(self.driver)
            cmcc.input_cmcc_username(key)#改为列表读取
            cmcc.input_cmcc_password(value)
            cmcc.click_cmcc_btn()
            #cmcc.get_screent_img()
            self.driver.implicitly_wait(5)
            #关闭提示框
            cmcc.click(['id','gViewCloseBtnGViewInfo'])
            time.sleep(2)

            #点击第一条待办
            self.driver.switch_to.frame('iframecontent-utsmain')
            self.driver.find_element_by_xpath("//*[@id='todo']/tbody/tr[" + str(1) + "]/td[3]/a").click()
            time.sleep(2)
            windows = self.driver.window_handles
            self.driver.switch_to.window(windows[1])
            self.driver.implicitly_wait(30)
            time.sleep(2)

            # 提交下一处理
            self.driver.find_element_by_xpath(next_xpath).click()
            time.sleep(2)

            #无需填写意见用户列于下方,按人物执行分支
            if key=='tanchun':
                #送办公厅核稿
                self.driver.find_element_by_xpath(commit_xpath).click()
                time.sleep(2)
                # 提交前确认框确认按钮
                self.driver.find_element_by_xpath(confirm_xpath).click()
                time.sleep(2)

            elif key=='youmingju':
                #取消提交下一处理
                self.driver.find_element_by_xpath('//*[@id="grcspSubmitWindow"]/div/div/div[3]/button[2]').click()
                time.sleep(2)
                #填写文件编号
                self.driver.find_element_by_xpath('//*[@id="postManager"]').click()
                time.sleep(2)
                self.driver.find_element_by_xpath('//*[@id="GEditInfoOkButton"]').click()
                time.sleep(2)
                # 再次提交下一处理
                self.driver.find_element_by_xpath(next_xpath).click()
                time.sleep(2)
                #送办公厅发送
                self.driver.find_element_by_xpath('//*[@id="grcsp_tran_li_sid-EBD5A282-BC4F-4DD8-A58A-A8643EDD4881"]/a').click()
                time.sleep(2)
                self.driver.find_element_by_xpath(commit_xpath).click()
                time.sleep(2)
                self.driver.find_element_by_xpath(confirm_xpath).click()
                time.sleep(2)

            elif key=='wanghuaguang':
                self.driver.find_element_by_xpath('//*[@id="grcspSubmitWindow"]/div/div/div[3]/button[2]').click()
                time.sleep(2)
                #发送文件
                self.driver.find_element_by_xpath('//*[@id="send"]').click()
                time.sleep(2)
                #纪检组监察室
                self.driver.find_element_by_xpath('//*[@id="dept"]/li[14]').click()
                time.sleep(2)
                self.driver.find_element_by_xpath('//*[@id="GEditInfoOkButton"]').click()
                time.sleep(2)
                # 循环获取alert弹窗，取到则退出循环；
                while cmcc.is_alert_present() == False:
                    pass
                cmcc.click_alert()

            else:
                # try点选同意单选框，点不到说明是普通意见，在意见框输入1
                try:
                    self.driver.find_element_by_xpath(agree_xpath).click()
                except Exception as e:
                    self.driver.find_element_by_xpath(text_xpath).send_keys(1)
                time.sleep(1)

                #按人物执行分支
                if key == 'fangfang':
                    #送公司领导签发
                    self.driver.find_element_by_xpath('//*[@id="grcsp_tran_li_sid-6EB1D400-B1D5-4485-BB57-DF190B132BD6"]/a').click()
                    time.sleep(1)
                    self.driver.find_element_by_xpath(commit_xpath).click()
                    time.sleep(2)
                    #选人界面确认按钮
                    self.driver.find_element_by_xpath('//*[@id="grcsp_selectItemsSubmitButton"]').click()
                    time.sleep(2)
                    #提交前确认框确认按钮
                    self.driver.find_element_by_xpath(confirm_xpath).click()
                    time.sleep(2)

                if key == 'shangbing':
                    #送办公厅处理
                    self.driver.find_element_by_xpath(commit_xpath).click()
                    time.sleep(2)
                    self.driver.find_element_by_xpath(confirm_xpath).click()
                    time.sleep(2)

            # 循环获取alert弹窗，取到则退出循环
            while cmcc.is_alert_present()==False:
                pass
            cmcc.click_alert()

            cmcc.change_to_window(0)
            cmcc.close()

    @classmethod
    def tearDownClass(cls):
        pass

    def tearDown(self):
        pass

if __name__ == "__main__":
    unittest.main()