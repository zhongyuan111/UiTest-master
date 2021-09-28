#!/usr/bin/env python3
# -*- coding:utf-8 -*-
from page.webpage import WebPage, sleep
from common.readelement import Element
# onetitle-一级标题   title_二级标题  cz_活动管理中操作  pc_批次
elements = Element('callmanage')
onetitle_call = elements['外呼管理']
title_hdmanage = elements['活动管理']
home = elements['首页']
button_home = elements['主页']
# title_rwmanage = elements['任务管理']
cz_bjbutton = elements['编辑']
cz_pcbutton = elements['批次']
cz_rwbutton = elements['任务']
cz_ywmbbutton = elements['业务模板']
pc_upbatch = elements['上传批次']
pc_addone = elements['逐条添加']
pc_phone = elements['电话号码']
pc_button = elements['确定按钮']
pc_close = elements['关闭按钮']
pc_start = elements['启动批次']
pc_tongh = elements['通话按钮']
pc_alert_search = elements['通话查询']

title_thmanage = elements['通话管理']
search_camname = elements['活动查询']
select_camname = elements['活动选择']
search_batch = elements['批次查询']
select_batch = elements['批次选择']
search_button = elements['批次查询']
viewdetail = elements['通话管理详情']
statedetail = elements['详情状态']
search_th = elements['搜索按钮']

# 外呼活动title
class HdManage(WebPage):
    '''活动管理'''

    # def __init__(self,driver):
    #     super().__init__(driver)

    def click_hdmanage(self):
        """点击活动管理"""
        self.is_click(title_hdmanage)

    def click_bantch(self):
        """点击操作-批次"""
        self.is_click(cz_pcbutton)

    def click_upbantch(self):
        """点击上传批次"""
        self.is_click(pc_upbatch)

    def click_add(self):
        """点击逐条添加"""
        self.is_click(pc_addone)

    def input_phone(self, content):
        """输入手机号"""
        self.input_text(pc_phone, txt=content)
        sleep(1)

    def click_confirm(self):
        """点击确认按钮"""
        self.is_click(pc_button)
        sleep(1)

    def click_close(self):
        """点击确认后的关闭页面"""
        self.is_click(pc_close)

    def click_start(self):
        """点击启动活动"""
        self.is_click(pc_start)
        sleep(25)

    def click_th_search(self):
        """点击通话查看"""
        self.is_click(pc_tongh)
        sleep(2)

    def pc_alert_name(self):
        """查询条数文本"""
        textname1= self.element_text(pc_alert_search)
        #print("%%%%%%%%%%%%%%%%%%%%", textname1)
        return textname1


class ThManage(WebPage):
    '''通话管理'''

    def click_thmanage(self):
        """点击通话详情"""
        self.is_click(title_thmanage)

    def click_camName(self):
        """活动查询"""
        self.is_click(search_camname)

    def click_selectName(self):
        """活动选择"""
        self.is_click(select_camname)

    def click_batchName(self):
        """批次查询"""
        self.is_click(search_batch)

    def click_selectBatch(self):
        """批次选择"""
        self.is_click(select_batch)

    def click_viewdetail(self):
        """点击查看详情"""
        self.is_click(viewdetail)

    def click_searchbutton(self):
        """通话管理搜索按钮"""
        self.is_click(search_th)

    def detail_state(self):
        """通话详情状态显示"""
        textname1 = self.element_text(statedetail)
        # print("%%%%%%%%%%%%%%%%%%%%", textname1)
        return textname1




class CommonManage(WebPage):
    """活动管理中公共方法"""

    def click_refresh(self):
        self.refresh()
        sleep(2)

    def click_hdmanage_title(self):
        """外呼管理"""
        self.is_click(onetitle_call)

    def click_Home(self):
        """首页"""
        self.is_click(home)
        sleep(2)

    def click_ButtonHome(self):
        """回到主页"""
        self.is_click(button_home)
        sleep(2)






