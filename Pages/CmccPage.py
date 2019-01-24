#coding:utf-8
from selenium.webdriver.common.by import By
from Base.Selenium2 import BasePage

class CmccPage(BasePage):
    """
    在这里写定位器，通过元素属性定位元素对象
    """
    ###PC端元素###
    userName = (By.NAME,'userName')#定位用户名输入框
    passWord = (By.NAME,'password')#定位密码输入框
    loginButton = (By.NAME,'loginButton')  # 定位登录按钮


    ###移动端元素###
    userNameMobile = (By.XPATH,'//*[@id="loginForm"]/div[2]/label[1]/input')
    passWordMobile = (By.XPATH,'//*[@id="password"]')
    loginButtonMobile = (By.CSS_SELECTOR,'input.button')
    firstTodomb = (By.XPATH,'/html/body/ion-side-menus/ion-side-menu-content/ion-nav-view/ion-view/ion-tabs/ion-nav-view/ion-view/ion-nav-view/ion-view/ion-content/div[1]/ion-list/div/ion-item[1]')
    handleButton = (By.XPATH,'/html/body/ion-side-menus/ion-side-menu-content/ion-nav-view/ion-view[2]/ion-tabs/div[3]/div/ion-footer-bar')
    formText = (By.XPATH,'/html/body/ion-side-menus/ion-side-menu-content/ion-nav-view/ion-view[2]/ion-tabs/div[1]/ion-scroll/div/div/a[2]/span')

    # userList = {"daizhong":"cmcc1qaz2wsx",
    #             "wangxiaojie":"cmcc1qaz2wsx",
    #             "yanglin":"cmcc1qaz2wsx",
    #             "weibing":"cmcc1qaz2wsx",
    #             "fangli":"cmcc1qaz2wsx",
    #             "yuchengzhi":"cmcc1qaz2wsx",
    #             "xuhaiyong":"cmcc1qaz2wsx",
    #             "taotao":"123456",
    #             "xiongwenjian":"123456",
    #             "zhangtao":"cmcc1qaz2wsx",
    #             "yejianfei":"cmcc1qaz2wsx"
    #             }
    userList = {"daizhong": "Pa$$w0rd",
                "wangxiaojie": "Pa$$w0rd",
                "yanglin": "Pa$$w0rd",
                "weibing": "Pa$$w0rd",
                "fangli": "Pa$$w0rd",
                "yuchengzhi": "Pa$$w0rd",
                "xuhaiyong": "Pa$$w0rd",
                "taotao": "Pa$$w0rd",
                "xiongwenjian": "Pa$$w0rd",
                "zhangtao": "Pa$$w0rd",
                "yejianfei": "Pa$$w0rd"
                }
    userList_cshq = {"yaobo": "Pa$$w0rd",
                 " youmeng": "Pa$$w0rd",
                 " yangyong": "Pa$$w0rd",
                 "caixuhui": "Pa$$w0rd",
                 "lijinze": "Pa$$w0rd",
                 " wangwenchao": "Pa$$w0rd",
                 " caixuhui ": "Pa$$w0rd",
                 "youmeng ": "Pa$$w0rd"
                    }

    userList_bmhq = {" weilihong": "Pa$$w0rd",
                 " gaolingling": "Pa$$w0rd",
                 "wangxiaoyun": "Pa$$w0rd",
                 "chenyurong": "Pa$$w0rd",
                 " duqian": "Pa$$w0rd",
                 "yushudan": "Pa$$w0rd",
                 " guojian": "Pa$$w0rd",
                 "duqian ": "Pa$$w0rd",
                 " wangxiaoyun ": "Pa$$w0rd"
                    }

    userList_drqb = {"tanchun": "Pa$$w0rd",
                     "fangfang": "Pa$$w0rd",
                     "shangbing": "Pa$$w0rd",
                     "youmingju": "Pa$$w0rd",
                     "wanghuaguang": "Pa$$w0rd"
                    }
    def input_cmcc_username(self,text):
        self.send_key(self.userName,text)

    def input_cmcc_password(self, text):
        self.send_key(self.passWord,text)

    def input_cmcc_username_mb(self,text):
        self.send_key(self.userNameMobile,text)

    def input_cmcc_password_mb(self, text):
        self.send_key(self.passWordMobile,text)

    def click_cmcc_btn(self):
        self.click(self.loginButton)

    def click_cmcc_btn_mb(self):
        self.click(self.loginButtonMobile)

