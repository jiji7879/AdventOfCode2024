import unittest
import day8

class MyTestCase(unittest.TestCase):
    def test_part_one(self):
        self.assertEqual(4, day8.part1("day8SampleInput2.txt"))
        self.assertEqual(14, day8.part1("day8SampleInput1.txt"))

    def test_part_two(self):
        self.assertEqual(9, day8.part2("day8SampleInput3.txt"))
        self.assertEqual(34, day8.part2("day8SampleInput1.txt"))

if __name__ == '__main__':
    unittest.main()
