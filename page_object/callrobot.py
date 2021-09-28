#!/usr/bin/env python3
# -*- coding:utf-8 -*-
from page.webpage import WebPage, sleep
from common.readelement import Element

elements = Element('callrobot')
title_call = elements['智能外呼菜单']
manage_robot = elements['外呼机器人管理']
search_robot = elements['机器人查询']
search_button = elements['机器人查询按钮']
alert_search = elements['断言查询']
creat_flow = elements['创建版本']
class CallPage(WebPage):
    '''登录'''

    # def __init__(self,driver):
    #     super().__init__(driver)


    def click_title(self):
        """点击智能外呼菜单"""
        self.is_click(title_call)

    def click_manage_robot(self):
        """外呼机器人管理"""
        self.is_click(manage_robot)

    def input_search(self, content):
        """输入机器人信息"""
        self.input_text(search_robot, txt=content)
        sleep(1)

    def click_search_button(self):
        self.is_click(search_button)

    def alert_name(self):
        """查询条数文本"""
        textname1= self.element_text(alert_search)
        #print("%%%%%%%%%%%%%%%%%%%%", textname1)
        return textname1
    def manage_name(self):
        textname2= self.element_text(manage_robot)
        return textname2

    def click_creat_flow(self):
        """创建版本"""
        self.is_click(creat_flow)

    def click_refresh(self):
        self.refresh()
