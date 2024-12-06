import unittest
import day6


class MyTestCase(unittest.TestCase):
    def test_part_one(self):
        self.assertEqual(41, day6.part1("day6SampleInput.txt"))

    def test_part_two(self):
        self.assertEqual({(6, 3), (7, 6), (7, 7), (8, 1), (8, 3), (9, 7)}, day6.part2("day6SampleInput.txt"))

    def test_trapped_edge_case(self):
        map = day6.readInput("day6TrappedEdgeCase.txt")
        (x, y) = day6.findStartingPosition(map)
        guard = day6.Guard(map, (x, y), day6.Direction.up)
        self.assertEqual(False, guard.escape())


if __name__ == '__main__':
    unittest.main()
