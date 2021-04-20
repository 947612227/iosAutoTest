# -*- encoding: utf-8 -*-

# @File    : appium_demo.py
# @Time    : 2021/04/01 17:10:25
# @Author  : zhangjia
# @Version : 1.0
# @Contact : zhangjia@aixuexi.com

from appium import webdriver
from selenium.webdriver.support.wait import WebDriverWait  # 显示等待
from selenium.common.exceptions import NoSuchElementException 

class baseFun(object):
    """
    Appium移动端自动化测试基类\n
    1、初始化webdriver;\n
    2、xx
    """

    def __init__(self) -> None:
        """初始化全局变量"""
        print("欢迎使用Appium自动化测试")

    def driverInit(self,bag=None, desired_caps=None):
        """初始化驱动"""
        desired_caps = dict()
        desired_caps['platformName'] = "iOS"
        desired_caps['platformVersion'] = "12.4"
        desired_caps['deviceName'] = "6szj"
        desired_caps['app'] = "com.aixuexi.studenttest"
        desired_caps['udid'] = "8ed6c08969291a1c651ffbf0c443236246f9504f"
 
        self.driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)

        print("初始化APP完成，请等待")
        print(self.driver)
        return self.driver

    def waits(driver,  type, name, descript=None):
        """
        --隐示等待(默认15秒) + 元素定位--\n
        1、driver;\n
        2、type ==> 定位方式(accessibility_id,find_element_by_class_name)\n
        3、name ==> 元素值\n
        """
        print(driver)
        i = 15
        if driver == None or type == None or name == None:
            print("waits方法缺少参数")

        if type == "id":
            print("[使用", type, "]方式定位-->",descript)
            try:
                wait = WebDriverWait(driver, i).until(
                    lambda x: x.find_element_by_accessibility_id(name))
                # print("wait:",wait)

            except Exception as e:
                print("定位[",name,"]出现异常-->",descript)
                print(str(e))
                
                
            else:
                print("发现元素->" + descript + ":" + name)
                return driver.find_element_by_accessibility_id(name)

        elif type == "className":
            print("[使用", type, "]方式定位-->",descript)
            try:
                wait = WebDriverWait(driver, i).until(
                    lambda x: x.find_element_by_class_name(name))
                print("wait:", wait)
            except Exception as e:
                print("定位[",name,"]出现异常-->",descript)
                print(str(e))
            else:
                print("发现元素->" + descript + ":" + name)
                return driver.find_element_by_class_name(name)



    def is_element_exist(self,type,element):
        """
        判断元素是否存在\n
        type(str) : [id],[className]->定位方式\n
        element(str) : [元素名称]
        """
        if type == "id":
            try:
                self.driver.find_element_by_accessibility_id(element)
            except NoSuchElementException:
                print("False")
                return False
            else:
                print("True")
                return True


        elif type == "className":
            try:
                self.driver.find_element_by_class_name(element)
            except NoSuchElementException:
                print("False")
                return False
            else:
                return True
                print("True")
        else:
            print("False")
            return False