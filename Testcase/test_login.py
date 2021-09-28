#!/usr/bin/env python3
# -*- coding:utf-8 -*-
from selenium import webdriver
from page_object.login import LoginPage
from selenium.webdriver.support import expected_conditions as EC
from common.readconfig import ini
import time
import common.readexcel
data = common.readexcel.pd_read_excel('login')

import  pytest
import allure
# test_datas =[
#     ({"user_username": "13898085342","user_password": "Lingban2019" },'账号不存在，请确认后再登录','登录失败,账号错误'),
#     ({"user_username": "13898085342","user_password": "Lingban2019" },'账号不存在，请确认后再登录','登录失败,账号错误'),
# ]
#test_datas = [('{"user_username": "13898085342","user_password": "Lingban2019" }', '账号不存在，请确认后再登录', '登录失败,账号错误'), ('{"user_username": "13898085342","user_password": "Lingban2018" }', '登录成功', '账号正常')]

@allure.feature("租户端")   #功能模块
@allure.story("租户登录")   #功能模块下的分支
@allure.link("https://redmine.lingban.cn/")  #链接
@allure.title("{title}")
@pytest.mark.parametrize("username,user_password,expected,title",
                         data
                         )
def test_lg(username,user_password,expected,title):
    '''账号登录'''
    driver = webdriver.Chrome()
    login_page = LoginPage(driver)
    login_page.get_url('http://10.0.2.70:3000/')
    login_page.input_name(username)
    login_page.input_pwd(user_password)
    login_page.click_login()
    alert = driver.find_element_by_xpath("/html/body/div[@class='lb-message lb-message--error']/p[@class='lb-message__content']")
    #alert = alert.text
    print("********我是测试*************",alert.text)
    assert  alert.text == expected
    login_page.quit_browser()



if __name__ == '__main__':
    pytest.main(['TestCase/test_login.py'])




