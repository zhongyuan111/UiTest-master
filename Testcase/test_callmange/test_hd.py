#!/usr/bin/python
# -*- coding:utf8 -*-
from page_object.callmanage import HdManage,CommonManage,ThManage
import allure
import pytest
from common.parseExcelFile import ParsePdExcel
excel = ParsePdExcel()
test_datas = excel.pd_read_excel('phone')
print (test_datas)
# test_datas =[({"phone": "18800000001"},["共 1 条"],"外呼成功"),]


# @pytest.fixture(scope="class")
# #browser是conftest中定义的驱动调用
# def open (browser):
#     call = HdManage(browser)
#     call.click_refresh()



@allure.epic("外呼管理")
@allure.feature("活动管理")  # 功能模块
# @pytest.mark.usefixtures('open')
class TestCallRobot:
    @pytest.fixture(scope="function")
    def open(self,browser):
        call = HdManage(browser)
        callcommon = CommonManage(browser)
        callcommon.click_Home()
        callcommon.click_ButtonHome()
        callcommon.click_refresh()

    @allure.story("创建批次并启动") # 功能模块
    @allure.link("https://redmine.lingban.cn/")  # 链接
    @allure.title("{title}")
    @pytest.mark.parametrize("phone,expected,title",test_datas)
    @pytest.mark.usefixtures('open')
    def test_001(self,browser,phone,expected,title):
        """用例描述：创建批次外呼"""
        call = HdManage(browser)
        callcommon = CommonManage(browser)
        callcommon.click_hdmanage_title()
        call.click_hdmanage()
        call.click_bantch()
        call.click_upbantch()
        call.click_add()
        call.input_phone(phone)
        call.click_confirm()
        call.click_close()
        call.click_start()
        call.click_th_search()
        # print ("**********我是测试***********",expected)
        assert call.pc_alert_name() == expected


    @allure.story("通话管理-通话详情")  # 功能模块
    @allure.title("通话详情正常")
    @pytest.mark.usefixtures('open')
    def test_002(self,browser):
        """用例描述：查看通话详情"""
        callth = ThManage(browser)
        callcommon = CommonManage(browser)
        callcommon.click_hdmanage_title()
        callth.click_thmanage()
        callth.click_camName()
        callth.click_selectName()
        callth.click_searchbutton()
        callth.click_viewdetail()
        assert callth.detail_state() == '已接通'

#
#     @allure.story("查询机器人2")  # 功能模块
#     def test_002(self, browser):
#         call = HdManage(browser)
#         call.click_manage_robot()
#         call.input_search('短信修复问题')
#         call.click_search_button()
#         call.alert_name()
#         # print ("**********我是测试***********",call.alert_name())
#         assert call.alert_name() == "共 1 条"
#
# @allure.epic("智能外呼机器人")
# @allure.feature("第二个类")  # 功能模块
# @pytest.mark.usefixtures('open')
# class TestCallMage:
#
#     # def test_001(self,browser):
#     #     call = CallPage(browser)
#     #     call.click_title()
#     @allure.story("查询机器人3") # 功能模块
#     @allure.link("https://redmine.lingban.cn/")  # 链接
#     @allure.title("{title}")
#     @pytest.mark.parametrize("test_input,expected,title",test_datas)
#     def test_003(self,browser,test_input,expected,title):
#         call = CallPage(browser)
#         #call.click_title()
#         call.click_manage_robot()
#         call.input_search(test_input['robot_name'])
#         call.click_search_button()
#         call.alert_name()
#         #print ("**********我是测试***********",call.alert_name())
#         assert call.alert_name() == expected[0]
#
#     @allure.story("查询机器人4")  # 功能模块
#     def test_004(self, browser):
#         call = CallPage(browser)
#         call.click_manage_robot()
#         call.input_search('短信修复问题')
#         call.click_search_button()
#         call.alert_name()
#         # print ("**********我是测试***********",call.alert_name())
#         assert call.alert_name() == "共 1 条"

# if __name__ == '__main__':
#     pytest -n 3 --html=report.html --self-contained-html
#     #生成报告
#     pytest.main(['-s', '-q', 'test_search.py', '--alluredir', './Report/'])
#     #os.system("allure generate Report -o Report/html")
#     os.popen('allure generate ./Report/  -o ./Report/')
