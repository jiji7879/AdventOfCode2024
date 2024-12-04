import unittest
import day3

class MyTestCase(unittest.TestCase):
    def test_part_1(self):
        sampleText = "xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5))"
        self.assertEqual(161, day3.part1(sampleText))

    def test_part_2(self):
        sampleText = "xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))"
        self.assertEqual(48, day3.part2(sampleText))


if __name__ == '__main__':
    unittest.main()
