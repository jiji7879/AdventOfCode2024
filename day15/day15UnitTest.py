import unittest

import day15


class MyTestCase(unittest.TestCase):
    def test_part_one(self):
        self.assertEqual(2028, day15.part1("day15SampleInput1.txt"))
        self.assertEqual(10092, day15.part1("day15SampleInput2.txt"))

    def test_part_two(self):
        self.assertEqual(9021, day15.part1("day15SampleInput2.txt"))


if __name__ == '__main__':
    unittest.main()
