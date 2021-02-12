import unittest
from scripts import sample_script

class SampleTestCase(unittest.TestCase):
    def test_covered_function(self):
        x = [1,2,3]

        self.assertTrue(sample_script.covered_function(x))