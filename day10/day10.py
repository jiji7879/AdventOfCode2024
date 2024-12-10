def readFileAsTopographicMap(filename: str) -> list:
    f = open(filename, "r")
    topographicMap = []
    for line in f.readlines():
        row = list(line.strip())
        rowInts = []
        for char in row:
            rowInts.append(int(char))
        topographicMap.append(rowInts)
    f.close()
    return topographicMap

# def findAllTrailheads(map: list, start: (int, int)):
#     trailPath = [set() for _ in range(10)]
#     trailPath[0].add(start)
#     for i in range(9):
#         for coordinate in trailPath[i]:
#             if 0 <= coordinate[0]+1 < len(map) and map[coordinate[0]+1][coordinate[1]] == i+1:
#                 trailPath[i+1].add((coordinate[0]+1, coordinate[1]))
#             if 0 <= coordinate[0]-1 < len(map) and map[coordinate[0]-1][coordinate[1]] == i+1:
#                 trailPath[i+1].add((coordinate[0]-1, coordinate[1]))
#             if 0 <= coordinate[1] + 1 < len(map[coordinate[0]]) and map[coordinate[0]][coordinate[1]+1] == i+1:
#                 trailPath[i+1].add((coordinate[0], coordinate[1]+1))
#             if 0 <= coordinate[1] - 1 < len(map[coordinate[0]]) and map[coordinate[0]][coordinate[1]-1] == i+1:
#                 trailPath[i+1].add((coordinate[0], coordinate[1]-1))
#     return len(trailPath[-1])

def findAllTrails(map: list, start: (int, int), onlyDistinctEndpoints: bool):
    trailPath = [dict() for _ in range(10)]
    trailPath[0][start] = 1
    for i in range(9):
        for coordinate in trailPath[i]:
            if 0 <= coordinate[0]+1 < len(map) and map[coordinate[0]+1][coordinate[1]] == i+1:
                if (coordinate[0]+1, coordinate[1]) not in trailPath[i+1]:
                    trailPath[i+1][(coordinate[0]+1, coordinate[1])] = trailPath[i][coordinate]
                else:
                    trailPath[i + 1][(coordinate[0] + 1, coordinate[1])] += trailPath[i][coordinate]
            if 0 <= coordinate[0]-1 < len(map) and map[coordinate[0]-1][coordinate[1]] == i+1:
                if (coordinate[0]-1, coordinate[1]) not in trailPath[i+1]:
                    trailPath[i + 1][(coordinate[0] - 1, coordinate[1])] = trailPath[i][coordinate]
                else:
                    trailPath[i + 1][(coordinate[0] - 1, coordinate[1])] += trailPath[i][coordinate]
            if 0 <= coordinate[1] + 1 < len(map[coordinate[0]]) and map[coordinate[0]][coordinate[1]+1] == i+1:
                if (coordinate[0], coordinate[1]+1) not in trailPath[i+1]:
                    trailPath[i + 1][(coordinate[0], coordinate[1]+1)] = trailPath[i][coordinate]
                else:
                    trailPath[i + 1][(coordinate[0], coordinate[1] + 1)] += trailPath[i][coordinate]
            if 0 <= coordinate[1] - 1 < len(map[coordinate[0]]) and map[coordinate[0]][coordinate[1]-1] == i+1:
                if (coordinate[0], coordinate[1]-1) not in trailPath[i+1]:
                    trailPath[i + 1][(coordinate[0], coordinate[1]-1)] = trailPath[i][coordinate]
                else:
                    trailPath[i + 1][(coordinate[0], coordinate[1] - 1)] += trailPath[i][coordinate]
    if onlyDistinctEndpoints:
        return len(trailPath[-1])

    counter = 0
    for coordinate in trailPath[-1]:
        counter += trailPath[-1][coordinate]
    return counter

def part1(filename: str) -> int:
    topographicMap = readFileAsTopographicMap(filename)
    counter = 0
    for i in range(len(topographicMap)):
        for j in range(len(topographicMap[i])):
            if topographicMap[i][j] == 0:
                x = findAllTrails(topographicMap, (i, j), True)
                counter += x
    return counter

def part2(filename: str) -> int:
    topographicMap = readFileAsTopographicMap(filename)
    counter = 0
    for i in range(len(topographicMap)):
        for j in range(len(topographicMap[i])):
            if topographicMap[i][j] == 0:
                x = findAllTrails(topographicMap, (i, j), False)
                counter += x
    return counter

if __name__ == "__main__":
    print(part1("day10Input.txt"))
    print(part2("day10Input.txt"))
