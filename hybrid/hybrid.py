#usr/bin/python
#encoding:utf-8
import time
from appium import webdriver
import unittest


class MyTestCase(unittest.TestCase):


    def setUp(self):
        desired_caps = {}
        desired_caps['platformName'] = 'Android'
        desired_caps['platformVersion'] = '4.3'
        desired_caps['deviceName'] = '192.168.33.101:5555'#adb devices
        desired_caps['appPackage'] = 'com.android.calculator2'# adb logcat |findstr START
        desired_caps['appActivity'] = '.Calculator'
        desired_caps["unicodeKeyboard"] = "True"  # 中文
        desired_caps["resetKeyboard"] = "True"
        desired_caps["automationName"] = "Selendroid"
        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)#发送指令，获取操作实例
    def tearDown(self):
        self.driver.quit()#释放资源
    def testAdd(self):
        number8=self.driver.find_element_by_id("digit8")
        number8.click()
        op=self.driver.find_element_by_id("plus")
        op.click()
        num5=self.driver.find_element_by_id("digit5")
        num5.click()
        equal=self.driver.find_element_by_id("equal")
        equal.click()
        try:
         result=self.driver.find_element_by_class_name("android.widget.EditText")
         value=result.text
         self.assertEqual('13',value)#判断是否相等
        except Exception:
          print (u'bug')
          self.fail("bug")




if __name__ == '__main__':
    unittest.main()

