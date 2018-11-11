import sys
import unittest
import Project3
from io import StringIO
import subprocess as sp

# Since processfile just prints errors to stderr, we can just check the length of 
# stderr on our test files to ensure that the error exists
class US30Tests(unittest.TestCase):
    def test_with_deceased(self):
        result = sp.Popen(['python', './src/Project3.py', './data/OneDeceased.ged'], stdout=sp.PIPE)

        out = str(result.communicate()[0])

        return self.assertTrue('MARRIED ALIVE INDIVIDUALS' in out) 


    def test_without_deceased(self):
        result = sp.Popen(['python', './src/Project3.py', './data/SmithFamilyNoMarried.ged'], stdout=sp.PIPE)

        out = str(result.communicate()[0])
        return self.assertTrue('MARRIED ALIVE INDIVIDUALS' not in out) 

if __name__ == '__main__':
    unittest.main()
