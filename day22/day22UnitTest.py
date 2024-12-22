import unittest

import day22


class MyTestCase(unittest.TestCase):
    def test_part_one(self):
        self.assertEqual(37327623, day22.part1("day22SampleInput.txt"))

    def test_part_two(self):
        self.assertEqual(23, day22.part2("day22SampleInput2.txt"))


if __name__ == '__main__':
    unittest.main()
