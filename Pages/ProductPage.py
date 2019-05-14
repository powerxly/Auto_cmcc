#coding:utf-8
from selenium.webdriver.common.by import By
from Base.Selenium2 import BasePage

class ProductPage(BasePage):
    """
    在这里写定位器，通过元素属性定位元素对象
    """
    ###PC端元素###
    # 定位用户名输入框
    userName = (By.ID,'username')
    # 定位密码输入框
    passWord = (By.ID,'password')
    # 定位登录按钮
    loginButton = (By.ID, 'login')
    # 定位个人工作台链接
    oaLink = (By.ID,'oa_link')
    # 应用管理
    appManager = (By.CSS_SELECTOR,'#applicationManageId > a')
    # 组织与权限
    orgAndauth = (By.CSS_SELECTOR,'#nav_sub > ul > li:nth-child(1) > h1 > i')
    # 组织管理
    orgManager = (By.CSS_SELECTOR,'#nav_sub > ul > li:nth-child(1) > div > div > dl:nth-child(1) > dd > a:nth-child(2)')
    # 组织机构新建页面确定按钮定位
    orgManagerCommitButton = (By.CSS_SELECTOR,'#systemDialogs > div > div > div >.modal-footer >button:nth-child(1)')
    # 用户管理
    userManager = (By.CSS_SELECTOR,'#nav_sub > ul > li:nth-child(1) > div > div > dl:nth-child(1) > dd > a:nth-child(1)')

    ###移动端元素###
    userNameMobile = (By.XPATH,'//*[@id="loginForm"]/div[2]/label[1]/input')
    passWordMobile = (By.XPATH,'//*[@id="password"]')
    loginButtonMobile = (By.CSS_SELECTOR,'input.button')
    firstTodomb = (By.XPATH,'/html/body/ion-side-menus/ion-side-menu-content/ion-nav-view/ion-view/ion-tabs/ion-nav-view/ion-view/ion-nav-view/ion-view/ion-content/div[1]/ion-list/div/ion-item[1]')
    handleButton = (By.XPATH,'/html/body/ion-side-menus/ion-side-menu-content/ion-nav-view/ion-view[2]/ion-tabs/div[3]/div/ion-footer-bar')
    formText = (By.XPATH,'/html/body/ion-side-menus/ion-side-menu-content/ion-nav-view/ion-view[2]/ion-tabs/div[1]/ion-scroll/div/div/a[2]/span')

    userListAdmin = {"admin":"admin"
                }
    userListHD = {"liyang":"李洋",
                    "diaojian":"刁健",
                    "hejia":"何佳",
                    "wangyu":"王禹",
                    "hanjingjing":"韩晶晶"
                    }

    userListBJHD = {"yangyi": "洋燚",
                      "liushuai": "刘帅",
                      "duyehui": "都业辉",
                      "zhaiying": "翟颖",
                      "lijia": "李佳"
                      }

    userListXAHD = {"zhangshasha":"张莎莎",
                    "liuxi":"刘嬉",
                    "dangshuwen":"党书文",
                    "tianxiaojing":"田小晶"
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

    orgListcodeHD = {"hdkj":"慧点科技"
                   }
    orgListcodeHDD = {"bjhdkj":"北京慧点科技",
                    "xahdkj":"西安慧点科技"
                    }


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

    def click_app_manager(self):
        self.click(self.appManager)

    def click_org_and_auth(self):
        self.click(self.orgAndauth)

    def click_org_manager(self):
        self.click(self.orgManager)

    def click_user_manager(self):
        self.click(self.userManager)

    def click_org_commit_button(self):
        self.click(self.orgManagerCommitButton)


