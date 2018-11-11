import Project3
import sys
import unittest
from io import StringIO


# Since processfile just prints errors to stderr, we can just check the length of 
# stderr on our test files to ensure that the error exists
class TestUniqueIDs(unittest.TestCase):
    def test_valid(self):
        old_stderr = sys.stderr
        old_stdout = sys.stdout

        result_err = StringIO()
        

        sys.stderr = result_err

        Project3.process_file("./data/SmithFamilyNoDeceased.ged")


        sys.stderr = old_stderr
        print(result_err.getvalue())

        self.assertTrue(len(result_err.getvalue()) == 0)

    def test_invalid(self):
        old_stderr = sys.stderr
        result = StringIO()
        sys.stderr = result
        Project3.process_file("./data/SmithFamilyErrors_Final.ged")
        sys.stderr = old_stderr

        self.assertTrue('US22' in result.getvalue())

if __name__ == '__main__':
    unittest.main()
