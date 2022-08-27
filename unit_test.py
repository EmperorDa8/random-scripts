from uppered import highlight_word
import unittest


class Test_Upper(unittest.TestCase):
    def test_format(self):
        test_case="Have a nice day", "dan" 
        expected="usman","dan"
        self.assertFalse(highlight_word(test_case),expected)
        
        

        
        
        
unittest.main()