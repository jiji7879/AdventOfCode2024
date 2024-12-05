import unittest
import day5


class MyTestCase(unittest.TestCase):
    def test_add_bad_pairing(self):
        self.assertEqual({45: [22]}, day5.addBadPairing({}, 22, 45))
        self.assertEqual({3: [1], 45: [22]}, day5.addBadPairing({3: [1]}, 22, 45))
        self.assertEqual({45: [1, 22]}, day5.addBadPairing({45: [1]}, 22, 45))

    def test_fix_page_ordering(self):
        self.assertEqual([1, 2, 3], day5.fixPageOrdering({3:[2], 2:[1]}, [3, 2, 1]))
        self.assertEqual([1, 2, 3], day5.fixPageOrdering({3: [2], 2: [1]}, [3, 1, 2]))
        self.assertEqual([1, 2, 3], day5.fixPageOrdering({3: [2], 2: [1]}, [2, 1, 3]))
        self.assertEqual([1, 2, 3], day5.fixPageOrdering({3: [2], 2: [1]}, [2, 3, 1]))
        self.assertEqual([1, 2, 3], day5.fixPageOrdering({3: [2], 2: [1]}, [1, 3, 2]))

    def test_part_1(self):
        self.assertEqual(143, day5.part1("day5SampleInput.txt"))

    def test_part_2(self):
        self.assertEqual(123, day5.part2("day5SampleInput.txt"))


if __name__ == '__main__':
    unittest.main()
