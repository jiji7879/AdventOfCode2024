import functools
import re

NUM_PAD_COORDINATES = {"7": (0, 0), "8": (0, 1), "9": (0, 2),
                       "4": (1, 0), "5": (1, 1), "6": (1, 2),
                       "1": (2, 0), "2": (2, 1), "3": (2, 2),
                       "0": (3, 1), "A": (3, 2)}

DIRECTIONAL_COORDINATES = {"^": (0, 1), "A": (0, 2), "<": (1, 0), "v": (1, 1), ">": (1, 2)}


@functools.lru_cache(None)
def numPadCode2(code: str, startingPosition: str = "A") -> list:
    newCode = []
    oldPosition = startingPosition
    for char in code:
        newPosition = char
        y_change = NUM_PAD_COORDINATES[newPosition][0] - NUM_PAD_COORDINATES[oldPosition][0]
        x_change = NUM_PAD_COORDINATES[newPosition][1] - NUM_PAD_COORDINATES[oldPosition][1]
        if y_change < 0 and NUM_PAD_COORDINATES[oldPosition][0] == 3 and NUM_PAD_COORDINATES[newPosition][1] == 0:
            newCode.append(("^", -y_change))
        if y_change > 0 and (NUM_PAD_COORDINATES[newPosition][0] != 3 or NUM_PAD_COORDINATES[oldPosition][1] != 0):
            newCode.append(("v", y_change))
        if x_change < 0:
            newCode.append(("<", -x_change))
        if x_change > 0:
            newCode.append((">", x_change))
        if y_change < 0 and (NUM_PAD_COORDINATES[oldPosition][0] != 3 or NUM_PAD_COORDINATES[newPosition][1] != 0):
            newCode.append(("^", -y_change))
        if y_change > 0 and (NUM_PAD_COORDINATES[newPosition][0] == 3 and NUM_PAD_COORDINATES[oldPosition][1] == 0):
            newCode.append(("v", y_change))
        oldPosition = char
        newCode.append(("A", 1))
    return newCode


@functools.lru_cache(None)
def directionalCode2(code: tuple[str, int], startingPosition: tuple[int, int] = DIRECTIONAL_COORDINATES["A"]) -> (
list, tuple[int, int]):
    newCode = []
    newPosition = DIRECTIONAL_COORDINATES[code[0]]
    y_change = newPosition[0] - startingPosition[0]
    x_change = newPosition[1] - startingPosition[1]
    if y_change > 0 and startingPosition[0] == 0 and newPosition[1] == 0:
        newCode.append(("v", y_change))
    if x_change > 0:
        newCode.append((">", x_change))
    if x_change < 0:
        newCode.append(("<", -x_change))
    if y_change > 0 and (startingPosition[0] != 0 or newPosition[1] != 0):
        newCode.append(("v", y_change))
    if y_change < 0 and (startingPosition[1] != 0 or newPosition[0] != 0):
        newCode.append(("^", -y_change))
    if y_change < 0 and (startingPosition[1] == 0 and newPosition[0] == 0):
        newCode.append(("^", -y_change))
    newCode.append(("A", code[1]))
    return newCode, newPosition


@functools.lru_cache(None)
def lengthHelper(startingMove: tuple[str, int], coordinateTuple, timesLeft: int):
    coordinateList = list(coordinateTuple)
    newCode, newCoordinate = directionalCode2(startingMove, coordinateList[0])
    if timesLeft > 1:
        length = 0
        for move in newCode:
            newLength, coordinateList = lengthHelper(move, tuple(coordinateList[1:]), timesLeft - 1)
            length += newLength
            coordinateList = [newCoordinate] + coordinateList
        return length, coordinateList
    else:
        length = 0
        for move in newCode:
            length += move[1]
        coordinateList[0] = newCoordinate
        return length, coordinateList


# to be tinkered with
def part2(times: int):
    puzzleInputs = ["965A", "143A", "528A", "670A", "973A"]
    score = 0
    for puzInput in puzzleInputs:
        match = re.findall("(\d+)A", puzInput)
        numeric = int(match[0])
        oldCode = numPadCode2(puzInput)
        newCoordinateList = [DIRECTIONAL_COORDINATES["A"] for i in range(times)]
        length = 0
        for tup in oldCode:
            # print(tup)
            newLength, newCoordinateList = lengthHelper(tup, tuple(newCoordinateList), times)
            length += newLength
        score += length * numeric
    return score


def sample():
    puzzleInputs = ["029A", "980A", "179A", "456A", "379A"]
    score = 0
    for puzInput in puzzleInputs:
        match = re.findall("(\d+)A", puzInput)
        numeric = int(match[0])
        oldCode = numPadCode2(puzInput)
        newCoordinateList = [DIRECTIONAL_COORDINATES["A"] for i in range(2)]
        length = 0
        for tup in oldCode:
            # print(tup)
            newLength, newCoordinateList = lengthHelper(tup, tuple(newCoordinateList), 2)
            length += newLength
        score += length * numeric
    return score


if __name__ == "__main__":
    # print(part1())
    print(part2(2))  # 222670
    print(sample())  # 126384
    print(part2(25))
    # 500891267954554 too high
    # 195385354492914 too low
    # 318108104950036 ?
    # 323564085117980
