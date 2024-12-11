import unittest
import day11


class MyTestCase(unittest.TestCase):
    def test_blink(self):
        self.assertEqual([1, 2024, 1, 0, 9, 9, 2021976], day11.blink([0, 1, 10, 99, 999]))  # add assertion here


if __name__ == '__main__':
    unittest.main()
