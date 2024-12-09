import unittest
import day9


class MyTestCase(unittest.TestCase):
    def test_part_one(self):
        self.assertEqual(1928, day9.part1("day9SampleInput.txt"))

    def test_part_two(self):
        self.assertEqual(2858, day9.part2("day9SampleInput.txt"))


if __name__ == '__main__':
    unittest.main()
