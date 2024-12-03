import unittest
import day3

class MyTestCase(unittest.TestCase):
    def test_part_1(self):
        sampleText = "xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5))"
        self.assertEqual(day3.part1(sampleText), 161)

    def test_part_2(self):
        sampleText = "xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))"
        self.assertEqual(day3.part2(sampleText), 48)


if __name__ == '__main__':
    unittest.main()
