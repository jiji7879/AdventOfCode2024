import re


class Computer:
    def __init__(self, registerA: int, registerB: int, registerC: int):
        self.registerA = registerA
        self.registerB = registerB
        self.registerC = registerC
        self.output = ""

    def __eq__(self, other):
        return self.registerA == other.registerA and self.registerB == other.registerB and self.registerC == other.registerC

    def combo_operand(self, operandNum: int) -> int:
        match operandNum:
            case 4:
                return self.registerA
            case 5:
                return self.registerB
            case 6:
                return self.registerC
            case _:
                if operandNum < 0 or operandNum > 6:
                    return 0
                else:
                    return operandNum

    def adv(self, operandNum: int):
        num = self.registerA
        den = 2 ** self.combo_operand(operandNum)
        self.registerA = num // den
        return

    def bxl(self, operandNum: int):
        self.registerB = self.registerB ^ operandNum
        return

    def bst(self, operandNum: int):
        self.registerB = self.combo_operand(operandNum) % 8
        return

    def jnz(self, operandNum: int, pointer: int) -> int:
        if self.registerA == 0:
            return pointer + 2
        else:
            return operandNum

    def bxc(self, operandNum: int):
        self.registerB = self.registerB ^ self.registerC
        return

    def out(self, operandNum: int):
        if self.output == "":
            self.output += str(self.combo_operand(operandNum) % 8)
        else:
            self.output += f",{str(self.combo_operand(operandNum) % 8)}"
        return

    def bdv(self, operandNum: int):
        num = self.registerA
        den = 2 ** self.combo_operand(operandNum)
        self.registerB = num // den
        return

    def cdv(self, operandNum: int):
        num = self.registerA
        den = 2 ** self.combo_operand(operandNum)
        self.registerC = num // den
        return

    def convertOutputToProgram(self) -> list:
        if self.output == "":
            return []
        program = self.output.split(",")
        for index in range(len(program)):
            program[index] = int(program[index])
        return program


def readComputerInputs(filename: str):
    f = open(filename, "r")
    program = []
    registers = [0, 0, 0]
    # we assume the input is absolutely correct
    lines = f.readlines()
    for i in range(len(lines)):
        line = lines[i]
        line = line.strip()
        registerA = re.findall("Register A: (\d+)", line)
        if len(registerA) > 0:
            registers[0] = int(registerA[0])
            continue
        registerB = re.findall("Register B: (\d+)", line)
        if len(registerB) > 0:
            registers[1] = int(registerB[0])
            continue
        registerC = re.findall("Register C: (\d+)", line)
        if len(registerC) > 0:
            registers[2] = int(registerC[0])
            continue
        instructions = re.findall("Program: ([0-9,]+)", line)
        if len(instructions) > 0:
            program = instructions[0].split(",")
            for index in range(len(program)):
                program[index] = int(program[index])
            continue
    f.close()
    return registers, program


def runProgram(program: list, computer: Computer):
    pointer = 0
    while pointer < len(program):
        match program[pointer]:
            case 0:
                computer.adv(program[pointer + 1])
                pointer += 2
            case 1:
                computer.bxl(program[pointer + 1])
                pointer += 2
            case 2:
                computer.bst(program[pointer + 1])
                pointer += 2
            case 3:
                pointer = computer.jnz(program[pointer + 1], pointer)
            case 4:
                computer.bxc(program[pointer + 1])
                pointer += 2
            case 5:
                computer.out(program[pointer + 1])
                pointer += 2
            case 6:
                computer.bdv(program[pointer + 1])
                pointer += 2
            case 7:
                computer.cdv(program[pointer + 1])
                pointer += 2
    return


def part1(filename: str) -> str:
    registers, program = readComputerInputs(filename)
    computer = Computer(registers[0], registers[1], registers[2])
    runProgram(program, computer)
    return computer.output


# part 2 work for my input
# [2, 4] -> B = A % 8
# [1, 5] -> B = B ^ 5 (0 <-> 5, 1 <-> 4, 2 <-> 7, 3 <-> 6)
# [7, 5] -> C = A // 2 ** B
# [0, 3] -> A = A // 8
# [4, 0] -> B = B ^ C
# [1, 6] -> B = B ^ 6 (0 <-> 6, 1 <-> 7, 2 <-> 4, 3 <-> 5)
# [5, 5] -> output += B % 8
# [3, 0] -> return back to the start unless A = 0
# output: 7,1,3,4,1,2,6,7,1

# simplifying?
# B = (A=0 <-> A=5, A=1 <-> A=4, A=2 <-> A=7, A=3 <-> A=6) % 8
# C = A // 2 ** (A=0 <-> A=5, A=1 <-> A=4, A=2 <-> A=7, A=3 <-> A=6) % 8
# B = (A=0 <-> A=5, A=1 <-> A=4, A=2 <-> A=7, A=3 <-> A=6) % 8 ^ (A // 2 ** (A=0 <-> A=5, A=1 <-> A=4, A=2 <-> A=7, A=3 <-> A=6) % 8)
# output += (B=0 mod 8 <-> B=6 mod 8, B=1 mod 8 <-> B=7 mod 8, B=2 mod 8 <-> B=4 mod 8, B=3 mod 8 <-> B=5 mod 8)
# A = A // 8

# if A = 0 mod 8
# C = A // 32
# B = 5 ^ (A // 32)
# output += (B=0 mod 8 <-> B=6 mod 8, B=1 mod 8 <-> B=7 mod 8, B=2 mod 8 <-> B=4 mod 8, B=3 mod 8 <-> B=5 mod 8)

# if A = 1 mod 8
# C = A // 16
# B = 4 ^ (A // 16)

# if A = 2 mod 8
# C = A // 128
# B = 7 ^ (A // 128)

# noting that each output requires A * 8, the smallest number is at least 8 ** 16 and at most 8 ** 17. Thank Python.
# There's something weird going on with mod 8s.
# Notably, if A // (8 ** math.floor(math.log(i, 8))) = 3, then the 0 is outputted at the end.
# In other words, the output is 3 * (8 ** 16) + x * (8 ** 15) + ...
# x = 0, 1, 5, 7, take the 0
# I hope it works, since I'm not sure if this generalizes to the C instruction

def findMinInverse(program: list) -> int:
    nums = [0]
    for outputLength in range(len(program)):
        if len(nums) == 0:
            return 0
        new_nums = []
        for i in range(8):
            for number in nums:
                computer = Computer(number + i, 0, 0)
                runProgram(program, computer)
                if computer.convertOutputToProgram() == program[-(outputLength + 1):]:
                    new_nums.append((number + i) * 8)
                    number += i
                    number *= 8
        nums = new_nums
    return min(nums) // 8


def part2(filename: str) -> int:
    registers, program = readComputerInputs(filename)
    return findMinInverse(program)


if __name__ == "__main__":
    print(part1("day17Input.txt"))
    print(part2("day17Input.txt"))
