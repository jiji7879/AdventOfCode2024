import unittest
import day13

class MyTestCase(unittest.TestCase):
    def test_part_one(self):
        self.assertEqual(480, day13.part1("day13SampleInput1.txt"))  # add assertion here


if __name__ == '__main__':
    unittest.main()
