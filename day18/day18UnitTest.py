import unittest

import day18


class MyTestCase(unittest.TestCase):
    def test_part_one(self):
        self.assertEqual(22, day18.part1("day18SampleInput1.txt", 12, (6, 6)))  # add assertion here


if __name__ == '__main__':
    unittest.main()
