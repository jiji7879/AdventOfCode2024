import unittest
import day12

class MyTestCase(unittest.TestCase):
    def test_part_one(self):
        self.assertEqual(140, day12.part1("day12SampleInput1.txt"))  # add assertion here
        self.assertEqual(772, day12.part1("day12SampleInput2.txt"))
        self.assertEqual(1930, day12.part1("day12SampleInput3.txt"))

    def test_part_two(self):
        self.assertEqual(236, day12.part2("day12SampleInput4.txt"))
        self.assertEqual(368, day12.part2("day12SampleInput5.txt"))
        self.assertEqual(1206, day12.part2("day12SampleInput3.txt"))


if __name__ == '__main__':
    unittest.main()
