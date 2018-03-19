import unittest
import  ddt

@ddt.ddt
class MyTestCase(unittest.TestCase):

    @ddt.data((1, 2), (2, 3))
    @ddt.unpack
    def test_something(self, value1, value2):
        print( value1, value2)
        self.assertEqual(value2, value1+1)

if __name__ == '__main__':
    unittest.main()