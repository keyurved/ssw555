import unittest

import datetime
import user_stories
from user_stories import *

class TestUS32(unittest.TestCase):
    def test_coming_up(self):
        date = datetime.datetime(1993, 11, 29)
        self.assertEqual(US31(date), True)
    def test_not_coming_up(self):
        date = datetime.datetime(1997, 8, 21)
        self.assertEqual(US31(date), False)