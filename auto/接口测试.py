# coding=utf-8
import urllib
import urllib2
url="http://reg.haibian.com/login/ajax_login"
data={}#字典,定义请求数据并赋值
data["loginname"]="student08@qq.com"
data["password"]="111111"
data=urllib.urlencode(data)#解码
request=url+'?'+data#字符串连接
response=urllib2.urlopen(request)#打开请求，获取对象
str=response.read()#读取服务器返回的数据
str=str.decode("unicode_escape")
print(str)




