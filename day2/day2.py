def makeLists(textfile: str):
    f = open(textfile, "r")
    lists = f.readlines()
    newList = []
    for list in lists:
        list.strip()
        numberSplit = list.split()
        for index in range(len(numberSplit)):
            numberSplit[index] = int(numberSplit[index])
        newList.append(numberSplit)
    f.close()

    return newList

#takes in an input of a list of lists (2D list)
def part1(lists: list):
    safeCount = 0
    for line in lists:
        safeCount += isLineSafePart1(line)
    return safeCount

#returns 1 if safe, 0 if unsafe
def isLineSafePart1(line: list):
    if len(line) < 2:
        return 0
    match isIncreasingOrDecreasing(line[0], line[1]):
        case 1:
            return isIncreasingLineSafe(line, 1, 3)
        case -1:
            # reverse the line changes from a decreasing check to increasing
            return isIncreasingLineSafe(line[::-1], 1, 3)
        case _:
            return 0

#returns 1 if safe, 0 if unsafe
def isIncreasingLineSafe(line: list, minDiff: int, maxDiff: int):
    for index in range(len(line) - 1):
        difference = line[index + 1] - line[index]
        if difference > maxDiff or difference < minDiff:
            return 0
    return 1

#returns 1 if increasing, -1 if decreasing, and 0 otherwise
def isIncreasingOrDecreasing(left: int, right: int):
    if left < right:
        return 1
    elif left > right:
        return -1
    else:
        return 0


def part2(lists: list):
    safeCount = 0
    for line in lists:
        safeCount += isLineSafePart2(line)
    return safeCount

#returns 1 if safe, 0 if unsafe
def isLineSafePart2(line: list):
    if len(line) < 2:
        return 0
    # should now get a general trend
    match isIncreasingOrDecreasing(line[0], line[-1]):
        case 1:
            return isIncreasingLineSafeWithOneBadLevel(line, 1, 3)
        case -1:
            # reverse the line changes from a decreasing check to increasing
            return isIncreasingLineSafeWithOneBadLevel(line[::-1], 1, 3)
        case _:
            return 0

#returns 1 if safe, 0 if unsafe
def isIncreasingLineSafeWithOneBadLevel(line: list, minDiff: int, maxDiff: int):
    safeOrUnsafe = []

    # compare every number in between
    for index in range(len(line) - 1):
        difference = line[index + 1] - line[index]
        if difference > maxDiff or difference < minDiff:
            safeOrUnsafe.append(0)
        else:
            safeOrUnsafe.append(1)

    match safeOrUnsafe.count(0):
        case 0:
            return 1

        # if only one unsafe, test both cases of removal
        # ex: [1, 3, 3, 5]
        # if multiple unsafes, the only way this can work is if there are two unsafes back to back
        # ex: [1, 5, 2, 3] or [3, 1, 5, 7]
        case 1 | 2:
            index = safeOrUnsafe.index(0)
            line1 = line[:index]+line[index+1:]
            line2 = line[:index+1]+line[index+2:]
            return max(isIncreasingLineSafe(line1, minDiff, maxDiff),
                           isIncreasingLineSafe(line2, minDiff, maxDiff))

        case _:
            return 0

if __name__ == "__main__":
    print(part1(makeLists("day2Input.txt")))
    print(part2(makeLists("day2Input.txt")))