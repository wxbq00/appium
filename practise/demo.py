from appium import webdriver
from time import sleep
import time

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

def view(self):
    time.sleep(5)
    webview=driver.contexts
    for i in webview:
        if 'WEBVIEW' in i:
            driver.switch_to.context(i)
            break
