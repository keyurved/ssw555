import unittest

import datetime
import user_stories
from user_stories import *

class TestUS16(unittest.TestCase):
    def testing_all_male_names_same(self):
        males = ["Danny Bibe", "Mike Bibe", "Tom Bibe"]
        self.assertEqual(US16(males), True)
    def test_no_males(self):
        self.assertEqual(US16([]), True)
    def test_diff_names(self):
        males = ["billy ken", "mike wiee"]
        self.assertEqual(US16(males), False)