#usr/bin/python
#encoding:utf-8
import time
from appium import webdriver

desired_caps ={}#获取手机app实例
desired_caps['platformName'] = 'Android'
desired_caps['platformVersion'] = '5.0.0'
desired_caps['deviceName'] = '192.168.56.101:5555'
desired_caps['appPackage'] = 'com.alpha.lagouapk'
desired_caps['appActivity'] = 'com.alpha.lagouapk.HelloActivity'
#desired_caps['app']=PATH('C:\Users\Administrator\Desktop\lagou.apk')
desired_caps["unicodeKeyboard"] = "True"#中文
desired_caps["resetKeyboard"] = "True"
driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
time.sleep(5)
driver.find_element_by_id('com.alpha.lagouapk:id/tv_login_by_type').click()
driver.find_element_by_id("com.alpha.lagouapk:id/et_four_guide_fragment_account").clear()
driver.find_element_by_id("com.alpha.lagouapk:id/et_four_guide_fragment_account").send_keys("13166427863")#resourceid
driver.find_element_by_id("com.alpha.lagouapk:id/et_four_guide_fragment_pwd").clear()
driver.find_element_by_id("com.alpha.lagouapk:id/et_four_guide_fragment_pwd").send_keys("369963")
driver.find_element_by_id("com.alpha.lagouapk:id/login_button").click()

try:
    if driver.find_element_by_id("com.alpha.lagouapk:id/login_button").is_displayed():#登陆成功后自动退出
        print ("fail")#登录失败
except Exception as e:
        print (e)
        print ("pass")

driver.quit()#释放资源
time.sleep(2)


