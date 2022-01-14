from gogex2 import format_name
import unittest


class Test_gogex2(unittest.TestCase):
    def test_format(self):
        test_case="dan","usman"
        expected="usman","dan"
        self.assertFalse(format_name(test_case,),expected)
        
        
    def test2(self):
        
        
        
unittest.main()