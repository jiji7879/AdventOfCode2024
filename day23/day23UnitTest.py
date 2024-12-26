import unittest

import day23


class MyTestCase(unittest.TestCase):
    def test_part_one(self):
        self.assertEqual(7, day23.part1("day23SampleInput1.txt"))

    def test_part_two(self):
        self.assertEqual("co,de,ka,ta", day23.part2("day23SampleInput1.txt"))


if __name__ == '__main__':
    unittest.main()
