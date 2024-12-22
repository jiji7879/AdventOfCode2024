import functools
from collections import defaultdict


def readNumbers(filename: str):
    f = open(filename, "r")
    numbers = []
    # we assume the input is absolutely correct
    lines = f.readlines()
    for i in range(len(lines)):
        line = lines[i]
        line = line.strip()
        numbers.append(int(line))
    f.close()
    return numbers


@functools.lru_cache(None)
def mix(given: int, secret: int):
    return given ^ secret


@functools.lru_cache(None)
def prune(secret: int):
    return secret % 16777216


@functools.lru_cache(None)
def nextSecret(secret: int):
    x = prune(mix(secret * 64, secret))
    y = prune(mix(x // 32, x))
    z = prune(mix(2048 * y, y))
    return z


@functools.lru_cache(None)
def finalSecret(secret: int):
    newSecret = secret
    for _ in range(2000):
        newSecret = nextSecret(newSecret)
    return newSecret


def part1(filename: str):
    numbers = readNumbers(filename)
    score = 0
    for number in numbers:
        score += finalSecret(number)
    return score


def secretDifferences(secret: int):
    list = []
    oldSecret = secret
    for _ in range(2000):
        newSecret = nextSecret(oldSecret)
        list.append((newSecret % 10) - (oldSecret % 10))
        oldSecret = newSecret
    return list


def createPatternList(listOfDifferences: list, initialValue: int):
    dictOfPatterns = {}
    for i in range(len(listOfDifferences) - 4):
        diffTuple = (listOfDifferences[i], listOfDifferences[i + 1], listOfDifferences[i + 2], listOfDifferences[i + 3])
        if diffTuple not in dictOfPatterns:
            dictOfPatterns[diffTuple] = initialValue + sum(listOfDifferences[:i + 4])
    return dictOfPatterns


def part2(filename: str):
    numbers = readNumbers(filename)
    ultimateDict = defaultdict(int)
    for number in numbers:
        secretDiff = secretDifferences(number)
        patternList = createPatternList(secretDiff, number % 10)
        for key, value in patternList.items():
            ultimateDict[key] += value
    maxValue = 0
    for value in ultimateDict.values():
        if value > maxValue:
            maxValue = value
    return maxValue


# this gtakes about a minute to run
if __name__ == "__main__":
    print(part1("day22Input.txt"))
    print(part2("day22Input.txt"))
