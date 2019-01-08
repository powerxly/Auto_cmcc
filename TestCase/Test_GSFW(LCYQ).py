# -*- coding: utf-8 -*-
# # # __author__ = 'duanhan'

#技术部-运维管理处 yaobo 起草后运行本代码
#youmeng 已提交部门会签

import unittest
from Pages.CmccPage import CmccPage
from Base.BrowserDriver import BrowserDriver
import time
import os.path
import yaml
from selenium.webdriver.common.action_chains import ActionChains

class CmccCase(unittest.TestCase):


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
        commit_xpath = temp['jcyj']['commit']
        save_xpath = temp['jcyj']['save']
        agree_xpath = temp['jcyj']['agree']
        disagree_xpath = temp['jcyj']['disagree']
        other_xpath = temp['jcyj']['other']
        confirm_xpath = temp['confirm']

        for key,value in CmccPage.userList2.items():
            driver = BrowserDriver(self)
            self.driver = driver.openbrowser(self)
            self.driver.implicitly_wait(30)
            openresult = 0
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

            #self.driver.find_element_by_xpath('//*[@id="zhuSong"]').send_keys('主送主送主送主送主送主送主送主送')
            #time.sleep(2)
            self.driver.find_element_by_xpath('//*[@id="processFormSubmitNext"]').click()
            time.sleep(2)
            self.driver.find_element_by_xpath(agree_xpath).click()
            time.sleep(2)
            self.driver.find_element_by_xpath(commit_xpath).click()
            time.sleep(2)
            self.driver.find_element_by_xpath('//*[@id="grcsp_left_cjs_deps_sid-0D8D7D61-88EB-4773-BFA7-ED6325A1BF66_3_switch"]').click()
            time.sleep(2)
            #yangyong杨永
            self.driver.find_element_by_xpath('//*[@id="grcsp_left_cjs_deps_sid-0D8D7D61-88EB-4773-BFA7-ED6325A1BF66_4_span"]').click()
            time.sleep(2)
            self.driver.find_element_by_xpath('//*[@id="grcsp_left_cjs_deps_sid-0D8D7D61-88EB-4773-BFA7-ED6325A1BF66_5_switch"]').click()
            time.sleep(2)
            #caixuhui蔡旭辉
            self.driver.find_element_by_xpath('//*[@id="grcsp_left_cjs_deps_sid-0D8D7D61-88EB-4773-BFA7-ED6325A1BF66_6_span"]').click()
            time.sleep(2)
            self.driver.find_element_by_xpath('//*[@id="grcsp_selectItemsSubmitButton"]').click()
            time.sleep(2)
            self.driver.find_element_by_xpath(confirm_xpath).click()
            time.sleep(10)
            # 获取alert弹窗
            try:
                dig_alert = self.driver.switch_to.alert
                time.sleep(1)
                # 关闭之
                dig_alert.accept()
                time.sleep(2)
            except Exception as e:
                print(Exception, ":", e)
                print('未弹出弹框')
            self.driver.switch_to.window(windows[0])
            cmcc.close()








            #点击第一条待办
            # self.driver.switch_to.frame('iframecontent-utsmain')
            # self.driver.find_element_by_xpath("//*[@id='todo']/tbody/tr[" + str(1) + "]/td[3]/a").click()
            # time.sleep(2)
            # windows = self.driver.window_handles
            # self.driver.switch_to.window(windows[1])
            # self.driver.implicitly_wait(30)
            # time.sleep(2)
            #
            # if key=='youmingju':
            #     #点击发送文件，选择政企分公司
            #     self.driver.find_element_by_xpath('//*[@id="send"]').click()
            #     time.sleep(2)
            #     self.driver.find_element_by_xpath('//*[@id="professionalFirms"]/li[5]').click()
            #     time.sleep(2)
            #     self.driver.find_element_by_xpath('//*[@id="GEditInfoOkButton"]').click()
            #     time.sleep(2)
            #     #获取alert弹窗
            #     while n:
            #         dig_alert = self.driver.switch_to.alert
            #         time.sleep(1)
            #     # 关闭之
            #         dig_alert.accept()
            #         time.sleep(2)
            #         n-=1
            #     self.driver.close()
            #
            # elif key=='wangyimeng':
            #     #点击填写文件编号
            #     self.driver.find_element_by_xpath('//*[@id="postManager"]').click()
            #     time.sleep(2)
            #     self.driver.find_element_by_xpath('//*[@id="GEditInfoOkButton"]').click()
            #     time.sleep(2)
            #
            #     #点击提交下一处理-分发文件
            #     self.driver.find_element_by_xpath('//*[@id="processFormSubmitNext"]').click()
            #     time.sleep(2)
            #     self.driver.find_element_by_xpath('// *[ @ id = "grcsp_tran_li_sid-956C3970-656F-4D0D-A539-D7B329FCEB50"] / a').click()
            #     time.sleep(2)
            #     self.driver.find_element_by_xpath('//*[@id="grcspSubmitWindow"]/div/div/div[3]/button[1]').click()
            #     time.sleep(2)
            #
            #     #选择所有处室负责人并确定
            #     address=self.driver.find_element_by_xpath('//*[@id="grcsp_left_multi_users_scope_sid-FC9B6E64-EB98-496C-B04E-4E6D09875CD7_9_span"]')
            #     ActionChains(self.driver).double_click(address).perform()
            #     time.sleep(2)
            #     self.driver.find_element_by_xpath('// *[ @ id = "grcsp_selectItemsSubmitButton"]').click()
            #     time.sleep(2)
            #     self.driver.find_element_by_xpath('// *[ @ id = "grcsp_submitInWindowButton"]').click()
            #     time.sleep(10)
            #     #获取alert弹窗
            #     dig_alert = self.driver.switch_to.alert
            #     time.sleep(1)
            #     # 关闭之
            #     dig_alert.accept()
            #     time.sleep(2)
            # self.driver.switch_to.window(windows[0])
            # cmcc.close()
            #testtest


    @classmethod
    def tearDownClass(cls):
        pass

    def tearDown(self):
        pass

if __name__ == "__main__":
    unittest.main()