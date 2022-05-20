from country import continet
import unittest

class Testcontinet(unittest.TestCase):
    def testbasic(self):
        testcase="isreal"
        expected="this is isreal"
        self.assertEquals(continet(testcase),expected)

    def testconnumber(self):
        testcase="nigeria"
        expected="this is nigeria"
        self.assertEqual(continet(testcase),expected)
unittest.main()