import math


# reusing a lot of day 16 code
def readMazeInputs(filename: str):
    f = open(filename, "r")
    walls = []
    # we assume the input is absolutely correct
    lines = f.readlines()
    for i in range(len(lines)):
        line = lines[i]
        line = line.strip().split(",")
        walls.append((int(line[0]), int(line[1])))
    f.close()
    return walls


def findNextMoves(startingCoordinate: (int, int), currentScore: int, walls: list, boardSize: (int, int)):
    listOfValidMoves = []
    north = (startingCoordinate[0] - 1, startingCoordinate[1])
    if north not in walls and 0 <= startingCoordinate[0] - 1 <= boardSize[0]:
        listOfValidMoves.append((north, currentScore + 1))

    south = (startingCoordinate[0] + 1, startingCoordinate[1])
    if south not in walls and 0 <= startingCoordinate[0] + 1 <= boardSize[0]:
        listOfValidMoves.append((south, currentScore + 1))

    west = (startingCoordinate[0], startingCoordinate[1] - 1)
    if west not in walls and 0 <= startingCoordinate[1] - 1 <= boardSize[1]:
        listOfValidMoves.append((west, currentScore + 1))

    east = (startingCoordinate[0], startingCoordinate[1] + 1)
    if east not in walls and 0 <= startingCoordinate[1] + 1 <= boardSize[1]:
        listOfValidMoves.append((east, currentScore + 1))
    return listOfValidMoves


# uses A-Star
def findEndAStar(walls: list, start: (int, int), end: (int, int), findMinScore: bool) -> int:
    dictOfSeenCells = {}
    cellsToBeCalculated = [(start, 0)]
    minScore = math.inf
    while len(cellsToBeCalculated) > 0:
        move, score = cellsToBeCalculated.pop(0)
        if move in dictOfSeenCells and dictOfSeenCells[move] < score:
            continue
        else:
            dictOfSeenCells[move] = score
        if move == end:
            if findMinScore and score < minScore:
                minScore = score
            elif not findMinScore:
                return score
            continue
        listOfValidMoves = findNextMoves(move, score, walls, end)
        for validMoves in listOfValidMoves:
            if (validMoves[0] not in dictOfSeenCells or dictOfSeenCells[validMoves[0]] > validMoves[1] and
                    validMoves[1] + (end[0] - validMoves[0][0]) + (end[1] - validMoves[0][1]) < minScore and
                    validMoves not in cellsToBeCalculated):
                cellsToBeCalculated.append(validMoves)
        cellsToBeCalculated = sorted(cellsToBeCalculated,
                                     key=lambda x: x[1] + (end[0] - x[0][0]) ** 2 + (end[1] - x[0][1]) ** 2)
    return minScore


def part1(filename: str, numWalls: int, destination: (int, int)) -> int:
    walls = readMazeInputs(filename)
    newWalls = walls[0:numWalls]
    return findEndAStar(newWalls, (0, 0), destination, True)


def part2(filename: str, startingNumWalls: int, destination: (int, int)) -> (int, int):
    walls = readMazeInputs(filename)
    newWalls = walls[0:startingNumWalls]
    for i in range(startingNumWalls, len(walls)):
        # if i % 10 == 0:
        # print(i)
        newWalls.append(walls[i])
        if findEndAStar(newWalls, (0, 0), destination, False) == math.inf:
            return walls[i]


if __name__ == "__main__":
    print(part1("day18Input.txt", 1024, (70, 70)))
    print(part2("day18Input.txt", 3030, (70, 70)))
