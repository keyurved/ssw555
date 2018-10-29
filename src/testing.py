import unittest

import datetime
import user_stories
from user_stories import *

class TestUS24(unittest.TestCase):
    def test_valid_date_1(self):
        self.assertEqual(US24("77-25-1231"), False)
        return
    def test_valid_date_2(self):
        self.assertEqual(US24("abad"), False)
        return
    def test_valid_date_3(self):
        self.assertEqual(US24("01-01-1990"), True)
        return
    def test_valid_date_4(self):
        self.assertEqual(US24("00-00-0000"), False)
        return
    def test_valid_date_5(self):
        self.assertEqual(US24("12-18-1975"), False)
        return

class TestUS23(unittest.TestCase):
    def test_unique_name_and_birth_1(self):
        info = [["Jane Doe", "03-12-1993"], ["Bora Bibe", "03-03-1992"], ["Jane Doe", "03-12-1993"], ["Ray Layland", "12-12-1990"]]
        self.assertEqual(US23(info), False)
        return
    def test_unique_name_and_birth_2(self):
        info = [["Jane Doe", "03-12-1993"], ["Bora Bibe", "03-03-1992"], ["Jane Doper", "03-12-1993"], ["Ray Layland", "12-12-1990"]]
        self.assertEqual(US23(info), True)
        return
    def test_unique_name_and_birth_3(self):
        info = [["Mary Meth", "03-12-1993"], ["Bora Bibe", "03-03-1992"], ["Jane Doe", "03-12-1993"], ["Mom", "12-12-1990"]]
        self.assertEqual(US23(info), True)
        return
    def test_unique_name_and_birth_4(self):
        info = [["Jane Doe", "03-12-1993"], ["Bora Bibe", "03-03-1992"], ["Dad", "03-12-1993"], ["Mom", "12-12-1990"]]
        self.assertEqual(US23(info), True)
        return
    def test_unique_name_and_birth_5(self):
        info = [["Jane Doe", "03-12-1993"], ["Bora Bibe", "03-03-1992"], ["Jane Doe", "03-12-1893"], ["Ray Layland", "12-12-1990"]]
        self.assertEqual(US23(info), True)
        return