import unittest

import day19

class MyTestCase(unittest.TestCase):
    def test_part_one(self):
        self.assertEqual(6, day19.part1("day19SampleInput1.txt"))  # add assertion here

    def test_part_two(self):
        self.assertEqual(16, day19.part2("day19SampleInput1.txt"))


if __name__ == '__main__':
    unittest.main()
