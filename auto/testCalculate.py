# coding=utf-8
from appium import webdriver

import unittest, time


class CalTest(unittest.TestCase):
    def setUp(self):
        desired_caps = {}
        desired_caps['platformName'] = 'Android'
        desired_caps['platformVersion'] = '5.0.0'
        desired_caps['deviceName'] = '192.168.56.101:5555'
        desired_caps['appPackage'] = 'com.android.calculator2'
        desired_caps['appActivity'] = '.Calculator'
        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)

    def tearDown(self):
        self.driver.quit()

    def test_add_aa(self):
        time.sleep(5)
        self.driver.find_element_by_name("1").click()

        self.driver.find_element_by_name("5").click()

        self.driver.find_element_by_name("9").click()

        self.driver.find_element_by_name("delete").click()

        self.driver.find_element_by_name("9").click()

        self.driver.find_element_by_name("5").click()

        self.driver.find_element_by_name("+").click()

        self.driver.find_element_by_name("6").click()
        # self.driver.find_element_by_name(name).send_keys()
        self.driver.find_element_by_name("=").click()
        # ela =self.driver.find_element_by_android_uiautomator('newUiSelector().description("Animation")')
        # self.assertIsNotNone(ela)
        # els=self.driver.find_elements_by_android_uiautomator('new UiSelector().clickable(true)')
        # self.assertIsInstance(els, list)
        # el1=self.driver.find_element_by_accessibility_id('Animation')
        # self.assertIsNotNone(el1)
        el = self.driver.find_element_by_class_name("android.widget.EditText").text
        # text=el.__getattribute__('text')
        self.assertEqual("1601", el)
        self.driver.lock(10)

        try:
            el = self.driver.find_element_by_accessibility_id(0)
        except Exception as e:
            els = self.driver.find_elements_by_class_name(id)
            #self.driver.scroll(origin_el, destination_el)
        if el is None:
            el = self.driver.find_element_by_accessibility_id(id)
        el.click()


if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(CalTest)
    unittest.TextTestRunner(verbosity=2).run(suite)