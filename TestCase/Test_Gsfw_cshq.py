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
            if key!='yaobo':
                #点击第一条待办
                self.driver.switch_to.frame('iframecontent-utsmain')
                self.driver.find_element_by_xpath("//*[@id='todo']/tbody/tr[" + str(1) + "]/td[3]/a").click()
                time.sleep(2)
                windows = self.driver.window_handles
                self.driver.switch_to.window(windows[1])
                self.driver.implicitly_wait(30)
                time.sleep(2)

                #提交下一处理
                self.driver.find_element_by_xpath(next_xpath).click()
                time.sleep(2)

                #按人物执行分支
                #youmeng尤梦提交会签分支
                if key=='youmeng':
                    #点击同意单选框
                    self.driver.find_element_by_xpath(agree_xpath).click()
                    time.sleep(1)
                    #点击提交
                    self.driver.find_element_by_xpath(commit_xpath).click()
                    time.sleep(2)
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
                    self.driver.find_element_by_xpath(agree_xpath).click()
                    time.sleep(1)
                    self.driver.find_element_by_xpath('//*[@id="grcsp_tran_li_sid-27932EF0-46A4-44A3-8D7D-1DAC7CF4B092"]/a').click()
                    time.sleep(1)
                    self.driver.find_element_by_xpath(commit_xpath).click()
                    time.sleep(2)
                    self.driver.find_element_by_xpath('//*[@id="grcsp_selectItemsSubmitButton"]').click()
                    time.sleep(2)
                    self.driver.find_element_by_xpath(confirm_xpath).click()
                    time.sleep(2)


                if key=='yangyong':
                    self.driver.find_element_by_xpath(agree_xpath).click()
                    time.sleep(1)
                    self.driver.find_element_by_xpath(commit_xpath).click()
                    time.sleep(2)
                    #处理“是否结束当前人处理”弹框
                    flag = 1
                    while flag:
                        try:
                            dig_alert = self.driver.switch_to.alert
                            flag=0
                        except Exception as e:
                            print("未取到弹框")
                            flag = 1
                    time.sleep(1)
                    dig_alert.accept()
                    time.sleep(2)


                # caixuhui蔡旭辉 送会签人员内部处理分支
                if key=='caixuhui':
                    self.driver.find_element_by_xpath(agree_xpath).click()
                    time.sleep(1)
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
                if key=='caixuhui ':
                    self.driver.find_element_by_xpath(agree_xpath).click()
                    time.sleep(1)
                    self.driver.find_element_by_xpath(commit_xpath).click()
                    time.sleep(2)
                    self.driver.find_element_by_xpath(confirm_xpath).click()
                    time.sleep(2)


                if key=='wangwenchao':
                    #填写会签意见，意见内容为“1”
                    self.driver.find_element_by_xpath(text_xpath).send_keys(1)
                    time.sleep(1)
                    self.driver.find_element_by_xpath(commit_xpath).click()
                    time.sleep(2)
                    #点掉wangwenchao
                    self.driver.find_element_by_xpath('//*[@id="grcsp_right_append_person_grcsp_append_processor_true"]/option').click()
                    time.sleep(1)
                    #选择bingtiefeng邴铁峰
                    self.driver.find_element_by_xpath('//*[@id="grcsp_left_append_person_grcsp_append_processor_true_2_span"]').click()
                    time.sleep(1)
                    self.driver.find_element_by_xpath('//*[@id="grcsp_selectItemsSubmitButton"]').click()
                    time.sleep(2)
                    self.driver.find_element_by_xpath(confirm_xpath).click()
                    time.sleep(2)


                if key=='lijinze':
                    self.driver.find_element_by_xpath(text_xpath).send_keys(1)
                    time.sleep(1)
                    self.driver.find_element_by_xpath('//*[@id="grcsp_tran_li_grcsp_append_processor_false"]/a').click()
                    time.sleep(1)
                    self.driver.find_element_by_xpath(commit_xpath).click()
                    time.sleep(2)
                    # 处理“是否结束当前人处理”弹框
                    flag = 1
                    while flag:
                        try:
                            dig_alert = self.driver.switch_to.alert
                            flag = 0
                        except Exception as e:
                            print("未取到弹框")
                            flag = 1
                    time.sleep(1)
                    dig_alert.accept()
                    time.sleep(2)


                if key=='bingtiefeng':
                    self.driver.find_element_by_xpath(text_xpath).send_keys(1)
                    time.sleep(1)
                    self.driver.find_element_by_xpath(commit_xpath).click()
                    time.sleep(2)
                    self.driver.find_element_by_xpath(confirm_xpath).click()
                    time.sleep(2)


            #起草
            else:
                # 鼠标悬停。
                ele = self.driver.find_element_by_xpath('//*[@id="nav_sub"]/ul/li[1]/h1/i')
                ActionChains(self.driver).move_to_element(ele).perform()
                time.sleep(2)
                self.driver.find_element_by_xpath('//*[@id="nav_sub"]/ul/li[1]/div/div/dl[1]/dd/a[3]').click()
                windows = self.driver.window_handles
                self.driver.switch_to.window(windows[1])
                self.driver.implicitly_wait(30)
                time.sleep(2)

                #填写表单
                self.driver.find_element_by_xpath('//*[@id="phone"]').send_keys('联系电话联系电话联系电话联系电话')
                time.sleep(1)
                self.driver.find_element_by_xpath('//*[@id="fileTitle"]').send_keys('文件标题文件标题文件标题文件标题')
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
            flag=1
            while flag:
                try:
                    dig_alert = self.driver.switch_to.alert
                    flag = 0
                except Exception as e:
                    print("未取到弹框")
                    flag = 1
            time.sleep(1)
            # 关闭之
            dig_alert.accept()
            time.sleep(2)

            self.driver.switch_to.window(windows[0])
            cmcc.close()

    @classmethod
    def tearDownClass(cls):
        pass

    def tearDown(self):
        pass

if __name__ == "__main__":
    unittest.main()