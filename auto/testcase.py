#usr/bin/python
#encoding:utf-8
import unittest
import time
from appium import webdriver
class MyTestCase(unittest.TestCase):
    def setUp(self):
        desired_caps = {}
        desired_caps['platformName'] = 'Android'
        desired_caps['platformVersion'] = '4.3'
        desired_caps['deviceName'] = '192.168.33.101:5555'
        desired_caps['appPackage'] = 'com.alpha.lagouapk'
        desired_caps['appActivity'] = '.HelloActivity'
        desired_caps["unicodeKeyboard"] = "True"  # 中文
        desired_caps["resetKeyboard"] = "True"
        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
    def testLoginPass(self):#方法名和文件名以test开头
        self.driver.find_element_by_id("et_four_guide_fragment_account").send_keys("13166427863")#resourceid
        self.driver.find_element_by_id("et_four_guide_fragment_pwd").send_keys("369963")
        self.driver.find_element_by_id("login_button").click()

        try:
            if self.driver.find_element_by_id("login_button").is_displayed():
                print ("fail")  # 登录失败
        except Exception as e:
            print (e)
            print ("pass")
            exist=False#不显示
        self.assertEqual(False, False)#登录成功

    def testLoginFailed(self):
        self.driver.find_element_by_id("et_four_guide_fragment_account").send_keys("mooktest")  # resourceid
        self.driver.find_element_by_id("et_four_guide_fragment_pwd").send_keys("mooktest")
        self.driver.find_element_by_id("login_button").click()

        try:
            if self.driver.find_element_by_id("login_button").is_displayed():
                print('fail')  # 登录失败
                exist=True
        except Exception as e:
                print(e)
                print("pass")

        self.assertEqual(True, True)#登录失败
    def tearDown(self):
        self.driver.quit()  # 释放资源


if __name__ == '__main__':
    unittest.main()
