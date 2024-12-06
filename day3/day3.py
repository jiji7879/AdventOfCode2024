import re

#groups the first two numbers in the regex of "mul(num1,num2)"
MUL_REGEX = r"mul\((\d{1,3}),(\d{1,3})\)"

#regex is split between 4 values
# first two are the numbers in the mul
# third is the possible "do()"
# fourth is the possible "don't()"
MUL_DO_DONT_REGEX = r"mul\((\d{1,3}),(\d{1,3})\)|(do\(\))|(don\'t\(\))"

def grabTextFromFile(textfile: str) -> str:
    f = open(textfile, "r")
    bigString = ""
    lists = f.readlines()
    for list in lists:
        bigString += list
    f.close()

    return bigString

def part1(string: str) -> int:
    matches = re.findall(MUL_REGEX, string)
    total = 0
    for pair in matches:
        total += int(pair[0]) * int(pair[1])
    return total

def part2(string: str) -> int:
    matches = re.findall(MUL_DO_DONT_REGEX, string)
    is_dont = False
    total = 0
    for group in matches:
        # if we find a "do()"
        if group[2] != "":
            is_dont = False
            continue
        # if we find a "don't()"
        elif group[3] != "":
            is_dont = True
            continue
        # otherwise the first two numbers should be filled, and check for don't logic
        if not is_dont and group[0] != "" and group[1] != "":
            total += int(group[0]) * int(group[1])
    return total

if __name__ == "__main__":
    text = grabTextFromFile("day3Input.txt")
    print(part1(text))
    print(part2(text))