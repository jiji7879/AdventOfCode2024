import unittest

import day20


class MyTestCase(unittest.TestCase):
    def test_part_one(self):
        self.assertEqual(1, day20.part1("day20SampleInput1.txt", 64))
        self.assertEqual(1, day20.part1("day20SampleInput1.txt", 60))
        self.assertEqual(5, day20.part1("day20SampleInput1.txt", 20))

    def test_part_two(self):
        self.assertEqual(3, day20.part2("day20SampleInput1.txt", 76))
        self.assertEqual(29, day20.part2("day20SampleInput1.txt", 72))


if __name__ == '__main__':
    unittest.main()
