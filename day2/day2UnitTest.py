import unittest
import day2


class MyTestCase(unittest.TestCase):

    def test_part_1(self):
        lists = day2.makeLists("day2SampleInput.txt")
        self.assertEqual(day2.part1(lists), 2)  # add assertion here

    def test_part_2(self):
        lists = day2.makeLists("day2SampleInput.txt")
        self.assertEqual(day2.part2(lists), 4)


if __name__ == '__main__':
    unittest.main()
