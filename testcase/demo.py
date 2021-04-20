# -*- encoding: utf-8 -*-

# @File    : demo.py
# @Time    : 2021/04/18 11:14:22
# @Author  : zhangjia 
# @Version : 1.0
# @Contact : zhangjia@aixuexi.com



from appium import webdriver

desired_caps = dict()
desired_caps['platformName'] = "iOS"
desired_caps['platformVersion'] = "12.4"
desired_caps['deviceName'] = "6szj"
desired_caps['app'] = "com.aixuexi.studenttest"
desired_caps['udid'] = "8ed6c08969291a1c651ffbf0c443236246f9504f"

driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)

# 同意 = driver.find_element_by_accessibility_id("同意").click()
# print(同意)
# 允许 = driver.find_element_by_accessibility_id("允许").click()
# print(允许)
driver.find_element_by_accessibility_id("密码登录").click()

driver.quit()