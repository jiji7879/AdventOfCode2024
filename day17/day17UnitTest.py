import unittest

import day17


class MyTestCase(unittest.TestCase):
    def test_part_one(self):
        self.assertEqual("4,6,3,5,6,3,5,2,1,0", day17.part1("day17SampleInput1.txt"))  # add assertion here

    def test_computer(self):
        computer1 = day17.Computer(0, 0, 9)
        day17.runProgram([2, 6], computer1)
        self.assertEqual(1, computer1.registerB)

        computer2 = day17.Computer(10, 0, 0)
        day17.runProgram([5, 0, 5, 1, 5, 4], computer2)
        self.assertEqual("0,1,2", computer2.output)

        computer3 = day17.Computer(2024, 0, 0)
        day17.runProgram([0, 1, 5, 4, 3, 0], computer3)
        self.assertEqual("4,2,5,6,7,7,7,7,3,1,0", computer3.output)
        self.assertEqual(0, computer3.registerA)

        computer4 = day17.Computer(0, 29, 0)
        day17.runProgram([1, 7], computer4)
        self.assertEqual(26, computer4.registerB)

        computer5 = day17.Computer(0, 2024, 43690)
        day17.runProgram([4, 0], computer5)
        self.assertEqual(44354, computer5.registerB)

        computer6 = day17.Computer(117440, 0, 0)
        day17.runProgram([0, 3, 5, 4, 3, 0], computer6)
        self.assertEqual([0, 3, 5, 4, 3, 0], computer6.convertOutputToProgram())


if __name__ == '__main__':
    unittest.main()
