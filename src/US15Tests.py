import unittest

import datetime
import user_stories
from user_stories import *

class TestUS15(unittest.TestCase):
    #for each family youd pass in the children
    def testing_less_than_15_siblings(self):
        siblings = ["@I38@, @I37@"]
        self.assertEqual(US15(siblings), True)
    def test_more_than_15_siblings(self):
        siblings = ["@I01@", "@I01@", "@I01@", "@I01@", "@I01@", "@I01@", "@I01@", "@I01@", "@I01@", "@I01@", "@I01@", "@I01@", "@I01@", "@I01@", "@I01@", "@I01@", "@I01@", "@I01@", "@I01@", "@I01@"]
        self.assertEqual(US15(siblings), False)