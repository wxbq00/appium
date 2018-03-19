#usr/bin/python
#encoding:utf-8
import time
from appium import webdriver
import unittest
from  ddt import ddt,data,unpack

@ddt
class MyTestCase(unittest.TestCase):
    def setUp(self):
        desired_caps = {}
        desired_caps['platformName'] = 'Android'
        desired_caps['platformVersion'] = '6.0.1'
        desired_caps['deviceName'] = '5728912e'
        desired_caps['appPackage'] = 'com.alpha.lagouapk'
        desired_caps['appActivity'] = '.HelloActivity'
        desired_caps["unicodeKeyboard"] = "True"
        desired_caps["resetKeyboard"] = "True"
        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)

    @data(("13166427863", "369963", False),#成功
          ("mooktest", "mooktest", True),#失败
          ("#$@%^", "735522@@", True))
    @unpack
    def testLogIn(self, username, password, expectedresult):#参数化
        self.driver.find_element_by_id("et_four_guide_fragment_account").send_keys("username")  # resourceid
        self.driver.find_element_by_id("et_four_guide_fragment_pwd").send_keys("password")
        self.driver.find_element_by_id("login_button").click()

        try:
            if self.driver.find_element_by_id("login_button").is_displayed():#存在按钮
                exist = True#失败
        except Exception as e:
            exist = False
        self.assertEqual(exist, expectedresult)

    def tearDown(self):
        self.driver.quit()

