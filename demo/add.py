from demo import cal
from demo.cal import Count
import unittest
class TestCount(unittest.TestCase):
    def setUp(self):
        print('setup')
    def test_add(self):
        j=Count(2,3)
        self.assertEqual(j.add(),5)
    def test_add2(self):
        j=Count(5,5)
        self.assertEqual(j.add(),10)
    def tearDown(self):
        print('end')
if __name__=='__main__':
    suite=unittest.TestSuite()
    suite.addTest(TestCount("test_add2"))
    runner=unittest.TextTestRunner()
    runner.run(suite)





