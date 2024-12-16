import math


def readMazeInputs(filename: str):
    start = (0, 0)
    end = (0, 0)
    f = open(filename, "r")
    walls = set()
    #moves = set()
    # we assume the input is absolutely correct
    lines = f.readlines()
    for i in range(len(lines)):
        line = lines[i]
        line = line.strip()
        for j in range(len(line)):
            if line[j] == '#':
                walls.add((i, j))
            #elif line[j] == '.':
                #moves.add((i, j))
            elif line[j] == 'S':
                start = (i, j)
            elif line[j] == 'E':
                end = (i, j)
    f.close()
    return walls, start, end

def scoreAddition(startingDirection: str, newDirection: str) -> int:
    if startingDirection != newDirection:
        return 1001
    else:
        return 1

# def findNextMoves(startingCoordinate: (int, int), startingDirection: str, currentScore: int, walls: set):
#     listOfValidMoves = []
#     north = (startingCoordinate[0]-1, startingCoordinate[1])
#     if north not in walls and startingDirection != "S":
#         listOfValidMoves.append(((north, "N"), currentScore + scoreAddition(startingDirection, "N")))
#
#     south = (startingCoordinate[0]+1, startingCoordinate[1])
#     if south not in walls and startingDirection != "N":
#         listOfValidMoves.append(((south, "S"), currentScore + scoreAddition(startingDirection, "S")))
#
#     west = (startingCoordinate[0], startingCoordinate[1]-1)
#     if west not in walls and startingDirection != "E":
#         listOfValidMoves.append(((west, "W"), currentScore + scoreAddition(startingDirection, "W")))
#
#     east = (startingCoordinate[0], startingCoordinate[1]+1)
#     if east not in walls and startingDirection != "W":
#         listOfValidMoves.append(((east, "E"), currentScore + scoreAddition(startingDirection, "E")))
#     return listOfValidMoves
#
# def findMinScore(walls: set, start: (int, int), end: (int, int)) -> int:
#     dictOfSeenCells = {}
#     cellsToBeCalculated = [((start, "E"), 0)]
#     minScore = math.inf
#     while len(cellsToBeCalculated) > 0:
#         move, score = cellsToBeCalculated.pop(0)
#         if move in dictOfSeenCells and dictOfSeenCells[move] < score:
#             continue
#         else:
#             dictOfSeenCells[move] = score
#         if move[0] == end:
#             if score < minScore:
#                 minScore = score
#             continue
#         listOfValidMoves = findNextMoves(move[0], move[1], score, walls)
#         for validMoves in listOfValidMoves:
#             if validMoves[1] < minScore:
#                 cellsToBeCalculated.append(validMoves)
#         cellsToBeCalculated = sorted(cellsToBeCalculated, key=lambda x: x[1])
#     return minScore

def part1(filename: str) -> int:
    walls, start, end = readMazeInputs(filename)
    return findMinScore2(walls, start, end)[0]

def findNextMoves2(startingCoordinate: (int, int), startingDirection: str, currentScore: int, walls: set, coordinatesStepped: set):
    listOfValidMoves = []
    north = (startingCoordinate[0]-1, startingCoordinate[1])
    if north not in walls and startingDirection != "S":
        listOfValidMoves.append(((north, "N"), currentScore + scoreAddition(startingDirection, "N"), coordinatesStepped.union({north})))

    south = (startingCoordinate[0]+1, startingCoordinate[1])
    if south not in walls and startingDirection != "N":
        listOfValidMoves.append(((south, "S"), currentScore + scoreAddition(startingDirection, "S"), coordinatesStepped.union({south})))

    west = (startingCoordinate[0], startingCoordinate[1]-1)
    if west not in walls and startingDirection != "E":
        listOfValidMoves.append(((west, "W"), currentScore + scoreAddition(startingDirection, "W"), coordinatesStepped.union({west})))

    east = (startingCoordinate[0], startingCoordinate[1]+1)
    if east not in walls and startingDirection != "W":
        listOfValidMoves.append(((east, "E"), currentScore + scoreAddition(startingDirection, "E"), coordinatesStepped.union({east})))
    return listOfValidMoves

def findMinScore2(walls: set, start: (int, int), end: (int, int)) -> (int, int):
    dictOfSeenCells = {}
    cellsToBeCalculated = [((start, "E"), 0, {start})]
    minScore = math.inf
    minScoreCoordinates = set()
    while len(cellsToBeCalculated) > 0:
        move, score, coordinates = cellsToBeCalculated.pop(0)
        if move in dictOfSeenCells and dictOfSeenCells[move] < score:
            continue
        else:
            dictOfSeenCells[move] = score
        if move[0] == end:
            if score < minScore:
                minScore = score
                minScoreCoordinates = coordinates
            elif score == minScore:
                minScoreCoordinates = minScoreCoordinates.union(coordinates)
            continue
        listOfValidMoves = findNextMoves2(move[0], move[1], score, walls, coordinates)
        for validMoves in listOfValidMoves:
            if validMoves[1] < minScore:
                cellsToBeCalculated.append(validMoves)
        cellsToBeCalculated = sorted(cellsToBeCalculated, key=lambda x: x[1])
    return minScore, len(minScoreCoordinates)

def part2(filename: str) -> int:
    walls, start, end = readMazeInputs(filename)
    return findMinScore2(walls, start, end)[1]

if __name__ == "__main__":
    walls, start, end = readMazeInputs("day16Input.txt")
    print(findMinScore2(walls, start, end))