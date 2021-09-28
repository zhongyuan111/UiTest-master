#!/usr/bin/python
# -*- coding:utf8 -*-
from page_object.callrobot import CallPage
import allure
import pytest
import os
from selenium import webdriver


test_datas =[({"robot_name": "自动化测试机器人"},["共 1 条"],"查询有数据"),]


@pytest.fixture(scope="class")
#browser是conftest中定义的驱动调用
def open (browser):
    call = CallPage(browser)
    call.click_refresh()



@allure.epic("智能外呼机器人")
@allure.feature("第一个类智能外呼机器人管理")  # 功能模块
@pytest.mark.usefixtures('open')
class TestCallRobot:

    # def test_001(self,browser):
    #     call = CallPage(browser)
    #     call.click_title()
    @allure.story("查询机器人1") # 功能模块
    @allure.link("https://redmine.lingban.cn/")  # 链接
    @allure.title("{title}")
    @pytest.mark.parametrize("test_input,expected,title",test_datas)
    def test_001(self,browser,test_input,expected,title):
        """用例描述：使用写好的入
        step1:点击机器人管理，输入机器人名字，点击查询"""
        call = CallPage(browser)
        call.click_title()
        call.click_manage_robot()
        call.input_search(test_input['robot_name'])
        call.click_search_button()
        call.alert_name()
        #print ("**********我是测试***********",call.alert_name())
        assert call.alert_name() == expected[0]

    @allure.story("查询机器人2")  # 功能模块
    def test_002(self, browser):
        call = CallPage(browser)
        call.click_manage_robot()
        call.input_search('短信修复问题')
        call.click_search_button()
        call.alert_name()
        # print ("**********我是测试***********",call.alert_name())
        assert call.alert_name() == "共 1 条"

@allure.epic("智能外呼机器人")
@allure.feature("第二个类")  # 功能模块
@pytest.mark.usefixtures('open')
class TestCallMage:

    # def test_001(self,browser):
    #     call = CallPage(browser)
    #     call.click_title()
    @allure.story("查询机器人3") # 功能模块
    @allure.link("https://redmine.lingban.cn/")  # 链接
    @allure.title("{title}")
    @pytest.mark.parametrize("test_input,expected,title",test_datas)
    def test_003(self,browser,test_input,expected,title):
        call = CallPage(browser)
        #call.click_title()
        call.click_manage_robot()
        call.input_search(test_input['robot_name'])
        call.click_search_button()
        call.alert_name()
        #print ("**********我是测试***********",call.alert_name())
        assert call.alert_name() == expected[0]

    @allure.story("查询机器人4")  # 功能模块
    def test_004(self, browser):
        call = CallPage(browser)
        call.click_manage_robot()
        call.input_search('短信修复问题')
        call.click_search_button()
        call.alert_name()
        # print ("**********我是测试***********",call.alert_name())
        assert call.alert_name() == "共 1 条"

# if __name__ == '__main__':
#     pytest -n 3 --html=report.html --self-contained-html
#     #生成报告
#     pytest.main(['-s', '-q', 'test_search.py', '--alluredir', './Report/'])
#     #os.system("allure generate Report -o Report/html")
#     os.popen('allure generate ./Report/  -o ./Report/')
