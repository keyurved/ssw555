import unittest

import datetime
import user_stories
from user_stories import *

class TestUS24(unittest.TestCase):
    def test_valid_date_1(self):
        self.assertEqual(US24("1 02 1995"), False)
        return
    def test_valid_date_2(self):
        self.assertEqual(US24("abad"), False)
        return
    def test_valid_date_3(self):
        self.assertEqual(US24("1 FEB 1995"), True)
        return
    def test_valid_date_4(self):
        self.assertEqual(US24("00-00-0000"), False)
        return
    def test_valid_date_5(self):
        self.assertEqual(US24("12-18-1975"), False)
        return