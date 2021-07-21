# -*- encoding: utf-8 -*-

# @File    : test_login.py
# @Time    : 2021/04/02 17:00:27
# @Author  : zhangjia
# @Version : 1.0
# @Contact : zhangjia@aixuexi.com

import sys,os
sys.path.append("/Users/admin/Documents/code/Python/appium/axx_iOS_autoTest/")
from common.basePage import baseFun
from time import sleep
import unittest


class TestCase(unittest.TestCase):
    """测试用例模块"""

    def setUp(self):
        """初始化unittest前置条件"""

        self.driver = baseFun().driverInit()
        self.wda = baseFun.waits
        # self.isElement = baseFun.is_element_exist #判断元素是否存在

    def tearDown(self):
        """初始化unittest后置条件"""
        self.driver.quit()

    def test_login(self):
        '''
        登录模块\n
        开始验证\n
        '''
        # self.wda(self.driver,"id","同意","安装后初次启动需要同意协议").click()
        if baseFun.is_element_exist(self,"id","温馨提示"):
            #ipa安装后首次启动的温馨提示和隐私政策
            print("首次启动点击同意按钮")
            self.wda(self.driver,"id","同意","安装后初次启动需要同意协议").click()
        else:
            print("不是首次启动,无需请求用户权限")


        #首次登陆 请求通知权限 不允许
        if baseFun.is_element_exist(self,"className","XCUIElementTypeAlert"):
            print("首次请求通知权限")
            self.wda(self.driver,"id","允许","安装后初次请求通知权限").click()

        else:
            print("不是首次启动,无需请求通知权限")
        # 定位切换到密码登录选项卡
        cs1 = self.wda(self.driver, "id", "密码登录", "切换到密码登录")
        cs1.click()

        #定位输入手机号的编辑框
        cs2 = self.wda(self.driver, "className", "XCUIElementTypeTextField", "定位手机号")
        cs2.clear()
        phone = "13488888888"
        print("手机号:", phone)
        cs2.send_keys(phone)

        #定位输入密码的编辑框
        cs3 = self.wda(self.driver, "className","XCUIElementTypeSecureTextField", "定位密码")
        passwd = "qwer1234"
        print("密码:", passwd)
        cs3.send_keys(passwd)

        #点击登录按钮
        # cs4 = self.wda(self.driver, "className","XCUIElementTypeButton", "定位登录按钮并点击")
        # cs4.click()

        cs4 = self.wda(self.driver, "id", "axxlogin loginBtn","点击登录按钮")
        cs4.click()



        #定位 选择学员角色 
        cs5 = self.wda(self.driver, "id", "张佳学员", "选择学员角色机构")
        cs5.click()

        #定位首次登陆弹出的领金币 右上角关闭按钮,首次登陆出现
        # cs6 = self.wda(self.driver, "className","XCUIElementTypeButton", "关闭弹出的首页赚金币任务")
        # cs6.click()

        #先判断是否有弹窗出现吧
        
        if baseFun.is_element_exist(self,"id","是否继续登录"):
            print("是否继续顶掉别人")

            

        #判断是否有首页任务存在 axxNotifition close
        if baseFun.is_element_exist(self,"id","axxNotifition close"):
            self.wda(self.driver, "id", "axxNotifition close", "关闭新手任务").click()



        #定位我的课程
        cs7 = self.wda(self.driver, "id", "我的课程", "点击我的课程")
        cs7.click()

        #定位学科菜单
        cs71 = self.wda(self.driver, "id", "学科", "定位左上角学科")
        cs71.click()

        cs72 = self.wda(self.driver, "id", "数学", "选择数学")
        cs72.click()

        #选择一节课
        cs73 = self.wda(self.driver, "className","XCUIElementTypeCell", "选择第一节课")
        cs73.click()


        # 定位 查看 电子讲义 
        cs10 = self.wda(self.driver, "id","去查看","定位'去查看'按钮")
        # cs10.click()
        
        #定位返回按钮
        cs11 = self.wda(self.driver, "id","axxNav GrayBack","定位'返回1'按钮")
        cs11.click()
    
        #定位返回按钮 需要两次返回
        cs11 = self.wda(self.driver, "id","axxNav GrayBack","定位'返回2'按钮")
        cs11.click()

        #定位我的
        cs12 = self.wda(self.driver, "id","我的","定位'我的'按钮")
        cs12.click()

        #引入JS滑动屏幕，因为退出登录按钮不在可视区域
        csjs01 = self.driver.execute_script('mobile: scroll', {'direction': 'down'})

        #定位设置
        cs13 = self.wda(self.driver, "id","设置","定位'设置'按钮")
        cs13.click()        

        #定位退出登录
        cs14 = self.wda(self.driver, "id","退出登录","定位'退出登录'按钮")
        cs14.click()    

        #定位确定退出登录
        cs14 = self.wda(self.driver, "id","确定","定位'确定-退出登录'按钮")
        cs14.click()  

        #退出后等一会再关闭
        sleep(5)
