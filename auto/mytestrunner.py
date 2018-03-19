#usr/bin/python
#encoding:utf-8
import auto.testcase
import  unittest

mysuite = unittest.TestSuite()
mysuite.addTest(auto.testcase.MyTestCase("testLoginFailed"))
mysuite.addTest(auto.testcase.MyTestCase("testLoginPass"))
#cases = unittest.TestLoader().loadTestsFromTestCase(testcase.MyTestCase)
#mysuite = unittest.TestSuite([cases])
#mysuite.addTest(unittestdemo.MyTestCase("testLogIn"))

myrunner = unittest.TextTestRunner(verbosity=2)#log输出输出级别
myrunner.run(mysuite)
