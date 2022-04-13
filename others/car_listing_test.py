#!/usr/bin/env python

from car_dict import car_listing
import unittest

class Test_Car_Listing(unittest.TestCase):
    def test_one(self):
        testcase= {"honda":9000,"ferrari":140000}
        expected="honda cost 9000 dollars, ferrari cost 140000 dollars"
        self.assertEqual(car_listing(testcase), expected)


#print(car_listing({"toyoya":5000,"lexus":9000}))

    def test_two(self):
        testcase=""
        expected=""
        self.assertEqual(car_listing(testcase), expected)

unittest.main()
