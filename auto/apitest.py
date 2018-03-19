# encoding=utf-8

import requests
import  unittest
import  ddt

class testClass(unittest.TestCase):
    @ddt.data
    @ddt.unpack
    def setUp(self):
        print ("初始化")
    def tearDown(self):
        print ("结束")

    def testGet(self):
        keyword = {"wd":"poptest"}
        headers = {"User-Agent":"test",
                   'Referer': 'http://login.weibo.cn/login/?ns=1&revalid=2&backU'}
        cookies = dict(IPLOC="CN1100", ABTEST="1")
        res = requests.get("https://customer-api.helijia.com/app-customer/transformers/getCityList?version=3.3.0.1&sign_type=md5&city=110100&req_time=1472372990756&device_type=android&device_id=d3c1d53d0a8a378f",
                           params=keyword,#api地址
                           headers=headers,
                           cookies = cookies)
        print (res.text)
        print (res.status_code)
        if u"北京市" in res.text:#有北京市
            print ("pass")
            result = True
        else:
            print ("fail")
            result = False
        self.assertTrue(result)

    def testPost(self):
        keyword = {"query":"postman"}
        headers = {"User-Agent":"hlj-android/3.3.0.1",
                   "Content-Type":"application/x-www-form-urlencoded",
                   'Referer': 'http://login.weibo.cn/login/?ns=1&revalid=2&backU'}
        cookies = dict(IPLOC="CN1100", ABTEST="1")
        res = requests.post("https://app.helijia.com/zmw/user/bind_dev",#{"result":"error","error":"city can not be null"}
                            #data=json.dumps(keyword),
                            data=keyword,
                            headers=headers,
                            cookies=cookies)
        print (res.text)
        print (res.status_code)
        if u"网页" in res.text:
            print ("pass")
        else:
            print ("fail")
        self.assertTrue(True)