import unittest
import day7

class MyTestCase(unittest.TestCase):
    def test_sample_input(self):
        arrayOfEquations = day7.readFileAsArrayOfEquations("day7SampleInput.txt")
        self.assertEqual(3749, day7.checkArrayOfEquations(arrayOfEquations, False))  # add assertion here
        self.assertEqual(11387, day7.checkArrayOfEquations(arrayOfEquations, True))


if __name__ == '__main__':
    unittest.main()
