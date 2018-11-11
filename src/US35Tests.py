import sys
import unittest
import Project3
from io import StringIO
import subprocess as sp

# Since processfile just prints errors to stderr, we can just check the length of 
# stderr on our test files to ensure that the error exists
class US35Tests(unittest.TestCase):
    def test_with_recently_born(self):
        result = sp.Popen(['python', './src/Project3.py', './data/SmithFamilyErrors_Final.ged'], stdout=sp.PIPE)

        out = str(result.communicate()[0])

        return self.assertTrue('BORN IN THE PAST 30 DAYS' in out) 


    def test_without_recently_born(self):
        result = sp.Popen(['python', './src/Project3.py', './data/SmithFamilyNoneRecentlyBorn.ged'], stdout=sp.PIPE)

        out = str(result.communicate()[0])
        return self.assertTrue('BORN IN THE PAST 30 DAYS' not in out) 

if __name__ == '__main__':
    unittest.main()