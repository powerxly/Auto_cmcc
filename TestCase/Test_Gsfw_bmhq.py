# -*- coding: utf-8 -*-
# # # __author__ = 'duanhan'

# 完成cshq（处室会签）脚本后再运行此脚本

import unittest
from Pages.CmccPage import CmccPage
from Base.BrowserDriver import BrowserDriver
import time
import os.path
import yaml
from selenium.webdriver.common.action_chains import ActionChains

class Test_Gsfw_bmhq(unittest.TestCase):


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


        for key,value in CmccPage.userList_bmhq.items():
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

            #weilihong魏丽红填写会签部门，然后提交会签分支
            if key==' weilihong':
                self.driver.find_element_by_xpath('//*[@id="cmoaJtDispatchDocEditForm"]/div[1]/fieldset[1]/div/table/tbody[2]/tr[8]/td[2]/div/div/span').click()
                time.sleep(2)
                # 技术部
                self.driver.find_element_by_xpath('//*[@id="huiQianChuShi"]/li[10]').click()
                time.sleep(1)
                # 内审部，注意技术部点选后，内审部位置上移
                self.driver.find_element_by_xpath('//*[@id="huiQianChuShi"]/li[11]').click()
                time.sleep(1)
                self.driver.find_element_by_xpath('//*[@id="GEditInfoOkButton"]').click()
                time.sleep(1)

            # 提交下一处理
            self.driver.find_element_by_xpath(next_xpath).click()
            time.sleep(2)

            # try点选同意单选框，点不到说明是普通意见，在意见框输入1
            try:
                self.driver.find_element_by_xpath(agree_xpath).click()
            except Exception as e:
                self.driver.find_element_by_xpath(text_xpath).send_keys(1)
            time.sleep(1)

            #列表设置key首位字符为空格，这类用户填完意见后直接提交
            if key[0] == ' ':
                self.driver.find_element_by_xpath(commit_xpath).click()
                time.sleep(2)

            #按人物执行分支
            if key == ' weilihong':
                #技术部选择wangxiaoyun王晓云
                self.driver.find_element_by_xpath('//*[@id="grcsp_left_cjs_deps_sid-3DEAF64F-FCF1-4206-9EF7-12D4C3E22530_1_switch"]').click()
                time.sleep(1)
                self.driver.find_element_by_xpath('//*[@id="grcsp_left_cjs_deps_sid-3DEAF64F-FCF1-4206-9EF7-12D4C3E22530_2_span"]').click()
                time.sleep(1)
                #gaolingling高玲玲
                self.driver.find_element_by_xpath('//*[@id="grcsp_left_cjs_deps_sid-3DEAF64F-FCF1-4206-9EF7-12D4C3E22530_3_switch"]').click()
                time.sleep(1)
                self.driver.find_element_by_xpath('//*[@id="grcsp_left_cjs_deps_sid-3DEAF64F-FCF1-4206-9EF7-12D4C3E22530_4_span"]').click()
                time.sleep(1)
                #选人界面确认按钮
                self.driver.find_element_by_xpath('//*[@id="grcsp_selectItemsSubmitButton"]').click()
                time.sleep(2)
                #提交前确认框确认按钮
                self.driver.find_element_by_xpath(confirm_xpath).click()
                time.sleep(2)

            if key == ' gaolingling':
                #送主办部门文书岗传递
                # 循环获取alert弹窗，取到则退出循环
                while cmcc.is_alert_present() == False:
                    pass
                cmcc.click_alert()

            if key == 'wangxiaoyun':
                self.driver.find_element_by_xpath('//*[@id="grcsp_tran_li_sid-0A7CA35C-B974-45C2-A02B-981CF098C0D1"]/a').click()
                time.sleep(1)
                self.driver.find_element_by_xpath(commit_xpath).click()
                time.sleep(2)
                self.driver.find_element_by_xpath('//*[@id="grcsp_left_cjs_deps_sid-741BE903-FEF2-4256-9AD7-7AFE106EFD6E_1_switch"]').click()
                time.sleep(1)
                #科技处-duqian杜倩
                self.driver.find_element_by_xpath('//*[@id="grcsp_left_cjs_deps_sid-741BE903-FEF2-4256-9AD7-7AFE106EFD6E_2_span"]').click()
                time.sleep(1)
                self.driver.find_element_by_xpath('//*[@id="grcsp_left_cjs_deps_sid-741BE903-FEF2-4256-9AD7-7AFE106EFD6E_9_switch"]').click()
                time.sleep(1)
                #资源管理处-chenyurong陈豫蓉
                self.driver.find_element_by_xpath('//*[@id="grcsp_left_cjs_deps_sid-741BE903-FEF2-4256-9AD7-7AFE106EFD6E_10_span"]').click()
                time.sleep(1)
                self.driver.find_element_by_xpath('//*[@id="grcsp_selectItemsSubmitButton"]').click()
                time.sleep(2)
                self.driver.find_element_by_xpath(confirm_xpath).click()
                time.sleep(2)

            if key == 'chenyurong':
                #送回相关部门会签
                self.driver.find_element_by_xpath('//*[@id="grcsp_tran_li_sid-0DEA2734-BBD7-4440-A416-F11E762F2CAF"]/a').click()
                time.sleep(1)
                self.driver.find_element_by_xpath(commit_xpath).click()
                time.sleep(2)
                while cmcc.is_alert_present() == False:
                    pass
                cmcc.click_alert()

            if key == ' duqian':
                #默认选中于书丹，再点选郭健
                self.driver.find_element_by_xpath('//*[@id="grcsp_left_multi_users_scope_sid-A7E0A0B8-19B5-44F9-8003-06DA2D88CDEC_3_span"]').click()
                time.sleep(1)
                self.driver.find_element_by_xpath('//*[@id="grcsp_selectItemsSubmitButton"]').click()
                time.sleep(2)
                self.driver.find_element_by_xpath(confirm_xpath).click()
                time.sleep(2)

            if key == 'yushudan':
                #结束办理
                self.driver.find_element_by_xpath('//*[@id="grcsp_tran_li_grcsp_append_processor_false"]/a').click()
                time.sleep(1)
                self.driver.find_element_by_xpath(commit_xpath).click()
                time.sleep(2)
                while cmcc.is_alert_present() == False:
                    pass
                cmcc.click_alert()

            if key == ' guojian':
                self.driver.find_element_by_xpath(confirm_xpath).click()
                time.sleep(2)

            if key == 'duqian ':
                self.driver.find_element_by_xpath('//*[@id="grcsp_tran_li_sid-BB86920E-B3D1-4EF6-BCF4-370D1D1D14B2"]/a').click()
                time.sleep(1)
                self.driver.find_element_by_xpath(commit_xpath).click()
                time.sleep(2)
                self.driver.find_element_by_xpath(confirm_xpath).click()
                time.sleep(2)

            if key == ' wangxiaoyun ':
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