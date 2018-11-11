import unittest

import datetime
import user_stories
from user_stories import *

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