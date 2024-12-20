def readRaceInputs(filename: str):
    start = (0, 0)
    end = (0, 0)
    f = open(filename, "r")
    board = []
    # we assume the input is absolutely correct
    lines = f.readlines()
    for i in range(len(lines)):
        line = lines[i]
        line = line.strip()
        for j in range(len(line)):
            if line[j] == 'S':
                start = (i, j)
            elif line[j] == 'E':
                end = (i, j)
        board.append(list(line))
    f.close()
    return board, start, end


def findRacePath(board: list, start: (int, int), end: (int, int)) -> list:
    path = [start]
    while path[-1] != end:
        path = findNextMove(path, board)
    return path


def findNextMoveHelper(path: list, board: list, coordinate: (int, int), forbidden: (int, int)) -> list:
    if (coordinate != forbidden and
            0 <= coordinate[0] <= len(board) and
            0 <= coordinate[1] <= len(board[coordinate[0]]) and
            board[coordinate[0]][coordinate[1]] != '#'):
        path.append(coordinate)
    return path


def findNextMove(path: list, board: list) -> list:
    startingCoordinate = path[-1]
    if len(path) > 1:
        forbidden = path[-2]
    else:
        forbidden = None

    north = (startingCoordinate[0] - 1, startingCoordinate[1])
    path = findNextMoveHelper(path, board, north, forbidden)
    if path[-1] != startingCoordinate:
        return path

    south = (startingCoordinate[0] + 1, startingCoordinate[1])
    path = findNextMoveHelper(path, board, south, forbidden)
    if path[-1] != startingCoordinate:
        return path

    west = (startingCoordinate[0], startingCoordinate[1] - 1)
    path = findNextMoveHelper(path, board, west, forbidden)
    if path[-1] != startingCoordinate:
        return path

    east = (startingCoordinate[0], startingCoordinate[1] + 1)
    path = findNextMoveHelper(path, board, east, forbidden)
    if path[-1] != startingCoordinate:
        return path
    return path


# startingCoordinate or startingCoordinateIndex does not need to be there
def findCheatFromCoordinate(path: list, startingCoordinate: (int, int), startingCoordinateIndex: int, threshold: int,
                            maxCheatLength: int) -> list:
    cheatPaths = []
    for endIndex in range(startingCoordinateIndex + threshold, len(path)):
        cheatLength = abs(path[endIndex][0] - startingCoordinate[0]) + abs(path[endIndex][1] - startingCoordinate[1])
        if cheatLength <= maxCheatLength and endIndex - startingCoordinateIndex - cheatLength >= threshold:
            cheatPaths.append((endIndex - startingCoordinateIndex - cheatLength, startingCoordinate, path[endIndex]))
    return cheatPaths


def findAllCheats(path: list, threshold: int, maxCheatLength: int) -> list:
    allCheats = []
    for index in range(len(path) - threshold):
        cheats = findCheatFromCoordinate(path, path[index], index, threshold, maxCheatLength)
        if len(cheats) > 0:
            for cheat in cheats:
                allCheats.append(cheat)
    return allCheats


def part1(filename: str, threshold: int) -> int:
    board, start, end = readRaceInputs(filename)
    path = findRacePath(board, start, end)
    allCheats = findAllCheats(path, threshold, 2)
    return len(allCheats)


def part2(filename: str, threshold: int) -> int:
    board, start, end = readRaceInputs(filename)
    path = findRacePath(board, start, end)
    allCheats = findAllCheats(path, threshold, 20)
    return len(allCheats)


if __name__ == "__main__":
    print(part1("day20Input.txt", 100))
    print(part2("day20Input.txt", 100))
