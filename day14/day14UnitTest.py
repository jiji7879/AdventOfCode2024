import unittest
import day14

class MyTestCase(unittest.TestCase):
    def teat_part_one(self):
        self.assertEqual(12, day14.part1("day14SampleInput1.txt", 11, 7, 100))  # add assertion here


if __name__ == '__main__':
    unittest.main()
