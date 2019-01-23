# -*- coding: utf-8 -*-
# # # __author__ = 'duanhan'

import unittest
from Pages.CmccPage import CmccPage
from Base.BrowserDriver import BrowserDriver
import time
import os.path
import yaml
from selenium.webdriver.common.action_chains import ActionChains

class Test_Gsfw_lcyq(unittest.TestCase):


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
        #保存意见按钮
        save_xpath = temp['jcyj']['save']
        #决策意见，同意单选框
        agree_xpath = temp['jcyj']['agree']
        #不同意单选框
        disagree_xpath = temp['jcyj']['disagree']
        #其他单选框
        other_xpath = temp['jcyj']['other']
        #提交前人员确认框，确认按钮
        confirm_xpath = temp['confirm']
        #提交下一处理按钮
        next_xpath = temp['next']
        #普通意见，意见输入框
        text_xpath = temp['ptyj']['textarea']

        now = time.strftime("%Y-%m-%d_%H_%M_%S")

        for key,value in CmccPage.userList2.items():
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

            #非起草人
            if key != 'yaobo':
                #点击第一条待办
                self.driver.switch_to.frame('iframecontent-utsmain')
                self.driver.find_element_by_xpath("//*[@id='todo']/tbody/tr[" + str(1) + "]/td[3]/a").click()
                time.sleep(2)
                self.driver.implicitly_wait(30)
                cmcc.change_to_window(1)

                #提交下一处理
                self.driver.find_element_by_xpath(next_xpath).click()
                time.sleep(2)

                # try点选同意单选框，点不到说明是普通意见，在意见框输入1
                try:
                    self.driver.find_element_by_xpath(agree_xpath).click()
                except Exception as e:
                    self.driver.find_element_by_xpath(text_xpath).send_keys(1)
                time.sleep(1)

                # 列表设置key首位字符为空格，这类用户填完意见后直接提交
                if key[0] == ' ':
                    self.driver.find_element_by_xpath(commit_xpath).click()
                    time.sleep(2)

                #按人物执行分支
                #youmeng尤梦提交会签分支
                if key==' youmeng':
                    self.driver.find_element_by_xpath('//*[@id="grcsp_left_cjs_deps_sid-0D8D7D61-88EB-4773-BFA7-ED6325A1BF66_3_switch"]').click()
                    time.sleep(1)
                    #选择yangyong杨永
                    self.driver.find_element_by_xpath('//*[@id="grcsp_left_cjs_deps_sid-0D8D7D61-88EB-4773-BFA7-ED6325A1BF66_4_span"]').click()
                    time.sleep(1)
                    self.driver.find_element_by_xpath('//*[@id="grcsp_left_cjs_deps_sid-0D8D7D61-88EB-4773-BFA7-ED6325A1BF66_5_switch"]').click()
                    time.sleep(1)
                    #caixuhui蔡旭辉
                    self.driver.find_element_by_xpath('//*[@id="grcsp_left_cjs_deps_sid-0D8D7D61-88EB-4773-BFA7-ED6325A1BF66_6_span"]').click()
                    time.sleep(1)
                    #选人界面确认按钮
                    self.driver.find_element_by_xpath('//*[@id="grcsp_selectItemsSubmitButton"]').click()
                    time.sleep(2)
                    #提交前确认框确认按钮
                    self.driver.find_element_by_xpath(confirm_xpath).click()
                    time.sleep(2)

                #会签完毕，提交主办领导分支
                if key=='youmeng ':
                    self.driver.find_element_by_xpath('//*[@id="grcsp_tran_li_sid-27932EF0-46A4-44A3-8D7D-1DAC7CF4B092"]/a').click()
                    time.sleep(1)
                    self.driver.find_element_by_xpath(commit_xpath).click()
                    time.sleep(2)
                    self.driver.find_element_by_xpath('//*[@id="grcsp_selectItemsSubmitButton"]').click()
                    time.sleep(2)
                    self.driver.find_element_by_xpath(confirm_xpath).click()
                    time.sleep(2)

                if key==' yangyong':
                    # 循环获取alert弹窗，取到则退出循环
                    while cmcc.is_alert_present() == False:
                        pass
                    cmcc.click_alert()

                # caixuhui蔡旭辉 送会签人员内部处理分支
                if key=='caixuhui':
                    self.driver.find_element_by_xpath('//*[@id="grcsp_tran_li_sid-03B187F8-F516-4E15-AB51-8A891188E3F0"]/a').click()
                    time.sleep(1)
                    self.driver.find_element_by_xpath(commit_xpath).click()
                    time.sleep(2)
                    #默认选中wangwenchao王文超，再点选lijinze李金泽
                    self.driver.find_element_by_xpath('//*[@id="grcsp_left_multi_users_scope_sid-9CB0E098-0227-49FD-9D9E-F57A7031F0B3_3_a"]').click()
                    time.sleep(1)
                    self.driver.find_element_by_xpath('//*[@id="grcsp_selectItemsSubmitButton"]').click()
                    time.sleep(2)
                    self.driver.find_element_by_xpath(confirm_xpath).click()
                    time.sleep(2)

                #送回部门领导审核分支
                if key==' caixuhui ' or key==' wangwenchao':
                    self.driver.find_element_by_xpath(confirm_xpath).click()
                    time.sleep(2)

                if key=='lijinze':
                    self.driver.find_element_by_xpath('//*[@id="grcsp_tran_li_grcsp_append_processor_false"]/a').click()
                    time.sleep(1)
                    self.driver.find_element_by_xpath(commit_xpath).click()
                    time.sleep(2)
                    while cmcc.is_alert_present() == False:
                        pass
                    cmcc.click_alert()


            #起草
            else:
                # 鼠标悬停。
                ele = self.driver.find_element_by_xpath('//*[@id="nav_sub"]/ul/li[1]/h1/i')
                ActionChains(self.driver).move_to_element(ele).perform()
                time.sleep(2)
                self.driver.find_element_by_xpath('//*[@id="nav_sub"]/ul/li[1]/div/div/dl[1]/dd/a[3]').click()
                self.driver.implicitly_wait(30)
                cmcc.change_to_window(1)
                time.sleep(2)

                #填写表单
                self.driver.find_element_by_xpath('//*[@id="phone"]').send_keys('13901234567')
                time.sleep(1)
                self.driver.find_element_by_xpath('//*[@id="fileTitle"]').send_keys('文件标题'+ now)
                time.sleep(1)
                self.driver.find_element_by_xpath('//*[@id="zhuSong"]').send_keys('主送主送主送主送主送主送主送主送')
                time.sleep(1)
                #令chrome浏览器可以编辑正文
                self.driver.execute_script('''$("input[name='attachmentZW']").val("正文正文正文正文正文正文正文正文");''')
                time.sleep(1)
                #提交下一处理
                self.driver.find_element_by_xpath(next_xpath).click()
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