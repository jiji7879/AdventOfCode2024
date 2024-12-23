import unittest
import day1


def makeSampleLists():
    leftList = [3, 4, 2, 1, 3, 3]
    rightList = [4, 3, 5, 3, 9, 3]
    return leftList, rightList


class TestPart1(unittest.TestCase):

    def test_part_1(self):
        leftList, rightList = makeSampleLists()
        self.assertEqual(11, day1.part1(leftList, rightList))

    def test_part_2(self):
        leftList, rightList = makeSampleLists()
        self.assertEqual(31, day1.part2(leftList, rightList))

if __name__ == '__main__':
    unittest.main()
