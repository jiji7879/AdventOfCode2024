import unittest
import day4


class MyTestCase(unittest.TestCase):
    def test_part_1(self):
        self.assertEqual(18, day4.part1("day4SampleInput.txt"))

    def test_part_2(self):
        self.assertEqual(9, day4.part2("day4SampleInput.txt"))


if __name__ == '__main__':
    unittest.main()
