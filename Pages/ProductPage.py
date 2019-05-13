#coding:utf-8
from selenium.webdriver.common.by import By
from Base.Selenium2 import BasePage

class ProductPage(BasePage):
    """
    在这里写定位器，通过元素属性定位元素对象
    """
    ###PC端元素###
    userName = (By.ID,'username')#定位用户名输入框
    passWord = (By.ID,'password')#定位密码输入框
    loginButton = (By.ID, 'login')  # 定位登录按钮
    oaLink = (By.ID,'oa_link')

    ###移动端元素###
    userNameMobile = (By.XPATH,'//*[@id="loginForm"]/div[2]/label[1]/input')
    passWordMobile = (By.XPATH,'//*[@id="password"]')
    loginButtonMobile = (By.CSS_SELECTOR,'input.button')
    firstTodomb = (By.XPATH,'/html/body/ion-side-menus/ion-side-menu-content/ion-nav-view/ion-view/ion-tabs/ion-nav-view/ion-view/ion-nav-view/ion-view/ion-content/div[1]/ion-list/div/ion-item[1]')
    handleButton = (By.XPATH,'/html/body/ion-side-menus/ion-side-menu-content/ion-nav-view/ion-view[2]/ion-tabs/div[3]/div/ion-footer-bar')
    formText = (By.XPATH,'/html/body/ion-side-menus/ion-side-menu-content/ion-nav-view/ion-view[2]/ion-tabs/div[1]/ion-scroll/div/div/a[2]/span')

    userList = {"admin":"admin"
                }
    # userList = {"daizhong": "Pa$$w0rd",
    #             "wangxiaojie": "Pa$$w0rd",
    #             "yanglin": "Pa$$w0rd",
    #             "weibing": "Pa$$w0rd",
    #             "fangli": "Pa$$w0rd",
    #             "yuchengzhi": "Pa$$w0rd",
    #             "xuhaiyong": "Pa$$w0rd",
    #             "taotao": "Pa$$w0rd",
    #             "xiongwenjian": "Pa$$w0rd",
    #             "zhangtao": "Pa$$w0rd",
    #             "yejianfei": "Pa$$w0rd"
    #             }
    # userList2 = {"youmingju": "Pa$$w0rd",
    #              "wangyimeng": "Pa$$w0rd",
    #              }
    def input_pdt_username(self,text):
        self.send_key(self.userName,text)

    def input_pdt_password(self, text):
        self.send_key(self.passWord,text)

    def input_pdt_username_mb(self,text):
        self.send_key(self.userNameMobile,text)

    def input_pdt_password_mb(self, text):
        self.send_key(self.passWordMobile,text)

    def click_pdt_btn(self):
        self.click(self.loginButton)

    def click_pdt_btn_mb(self):
        self.click(self.loginButtonMobile)

    def click_oa_link_button(self):
        self.click(self.oaLink)

