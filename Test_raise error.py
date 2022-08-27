import unittest
from raise_error import recharge


class Test_Word(unittest.TestCase):
    def test_one(self):
        network="mtn6"
        number="07034824573"
        expected=f"the {network} number is this {number}"
        self.assertEqual(recharge(network,number),expected)
        
        
    def test_two(self):
        network="airtel"
        number="0803405135790"
        expected=f"the {network} number is this {number}"
        self.assertAlmostEqual(recharge(network,number),expected)

unittest.main()
