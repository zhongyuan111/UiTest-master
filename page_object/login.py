from page.webpage import WebPage, sleep
from common.readelement import Element
from selenium import webdriver
#login = Element('login')

class LoginPage(WebPage):
    '''登录'''

    def __init__(self,driver):
        super().__init__(driver)
        elements = Element('login')
        self.username_input= elements['账号']
        self.pwd_input=elements['密码']
        self.click_button=elements['登录按钮']
        self.lg_text = elements['登录成功元素']


    def input_name(self, content):
        """输入账号"""
        self.input_text(self.username_input, txt=content)
        sleep()

    def input_pwd(self, content):
        """输入密码"""
        self.input_text(self.pwd_input, txt=content)
        sleep(1)

    def click_login(self):
        """点击搜索"""
        self.is_click(self.click_button)

    def quit_browser(self):
        """退出浏览器"""
        self.driver.quit()
        sleep(3)

    def login_text(self):
        """登录后的元素校验"""
        return self.element_text(self.lg_text)


if __name__ == '__main__':
    driver = webdriver.Chrome()
    login_page = LoginPage(driver)
    login_page.get_url('http://10.0.2.70:3000/')
    login_page.input_name('13898085347')
    login_page.input_pwd('Lingban2019')
    login_page.click_login()
    if login_page.login_text() == "":
        print("登录成功")  # 登录成功则跳出循环
        login_page.quit_browser()
    else:
        print("登录失败")


