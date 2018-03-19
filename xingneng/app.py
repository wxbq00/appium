#/usr/bin/python
#encoding:utf-8
import csv#读写csv文件
import os#操作系统
import time


class App(object):
    def __init__(self):#初始化函数
        self.content = ""
        self.startTime = 0

    #启动App
    def LaunchApp(self):
        cmd = 'adb shell am start -W -n com.android.browser/.BrowserActivity'#启动app命令
        self.content=os.popen(cmd)#从一个命令打开一个管道

    #停止App
    def StopApp(self):
        #cmd = 'adb shell am force-stop com.android.browser'
        cmd = 'adb shell input keyevent 3'#热启动停止
        os.popen(cmd)

    #获取启动时间
    def GetLaunchedTime(self):
        for line in self.content.readlines():#循环读取文件的内容
            if "ThisTime" in line:
                self.startTime = line.split(":")[1]#字符串分割
                break
        return self.startTime

#控制类
class Controller(object):
    def __init__(self, count):
        self.app = App()#获取app类实例
        self.counter = count#计数器
        self.alldata = [("timestamp", "elapsedtime")]#元祖

    #单次测试过程
    def testprocess(self):
        self.app.LaunchApp()
        # time.sleep(5)
        elpasedtime = self.app.GetLaunchedTime()
        self.app.StopApp()
        # time.sleep(3)
        currenttime = self.getCurrentTime()
        self.alldata.append((currenttime, elpasedtime))

    #多次执行测试过程
    def run(self):
        while self.counter >0:
            self.testprocess()
            self.counter = self.counter - 1#每次递减

    #获取当前的时间戳
    def getCurrentTime(self):
        currentTime = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())#返回以可读字符串表示的当地时间
        return currentTime

    #数据的存储
    def SaveDataToCSV(self):
        csvfile = open('startTime2.csv', 'wb')#以只写方式创建文件
        writer = csv.writer(csvfile)
        writer.writerows(self.alldata)#变成行
        csvfile.close()

if __name__ == "__main__":
    controller = Controller(10)#执行10次
    controller.run()
    controller.SaveDataToCSV()