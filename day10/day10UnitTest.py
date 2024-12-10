import unittest
import day10


class MyTestCase(unittest.TestCase):
    def test_part_one(self):
        self.assertEqual(1, day10.part1("day10SampleInput2.txt"))  # add assertion here
        self.assertEqual(36, day10.part1("day10SampleInput1.txt"))

    def test_part_two(self):
        self.assertEqual(81, day10.part2("day10SampleInput1.txt"))


if __name__ == '__main__':
    unittest.main()
