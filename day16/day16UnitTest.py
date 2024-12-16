import unittest

import day16


class MyTestCase(unittest.TestCase):
    def test_part_one(self):
        self.assertEqual(7036, day16.part1("day16SampleInput1.txt"))
        self.assertEqual(11048, day16.part1("day16SampleInput2.txt"))

    def test_part_one(self):
        self.assertEqual(45, day16.part2("day16SampleInput1.txt"))
        self.assertEqual(64, day16.part2("day16SampleInput2.txt"))


if __name__ == '__main__':
    unittest.main()