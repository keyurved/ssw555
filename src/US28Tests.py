import sys
import unittest
import Project3
from io import StringIO
import subprocess as sp

# Since processfile just prints errors to stderr, we can just check the length of 
# stderr on our test files to ensure that the error exists
class US28Tests(unittest.TestCase):
    def test_siblings_display(self):
        result = sp.Popen(['python', './Project3.py', '../data/SmithFamilyNoDeceased.ged'], stdout=sp.PIPE)

        out = str(result.communicate()[0])
        return self.assertTrue('SIBLINGS FROM FAMILY' not in out) 

if __name__ == '__main__':
    unittest.main()
