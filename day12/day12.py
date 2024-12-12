import copy

def readFileAsBoardOfCharacters(filename: str) -> list:
    f = open(filename, "r")
    boardOfCharacters = []
    for string in f.readlines():
        boardOfCharacters.append(list(string.strip()))
    f.close()
    return boardOfCharacters

def findRegions(boardOfCharacters: list) -> list:
    listOfCoordinatesToBeChecked = [(i, j) for j in range(len(boardOfCharacters[0])) for i in range(len(boardOfCharacters))]
    listOfRegions = []
    while len(listOfCoordinatesToBeChecked) > 0:
        startingCoordinate = listOfCoordinatesToBeChecked.pop(0)
        region = [startingCoordinate]
        regionType = boardOfCharacters[startingCoordinate[0]][startingCoordinate[1]]
        regionIndex = 0
        while regionIndex < len(region):
            currentCoordinate = region[regionIndex]
            #check all sides of the region
            try:
                down = (currentCoordinate[0]+1, currentCoordinate[1])
                if boardOfCharacters[down[0]][down[1]] == regionType and down in listOfCoordinatesToBeChecked:
                    listOfCoordinatesToBeChecked.remove(down)
                    region.append(down)
            except IndexError:
                pass
            try:
                up = (currentCoordinate[0]-1, currentCoordinate[1])
                if boardOfCharacters[up[0]][up[1]] == regionType and up in listOfCoordinatesToBeChecked:
                    listOfCoordinatesToBeChecked.remove(up)
                    region.append(up)
            except IndexError:
                pass
            try:
                left = (currentCoordinate[0], currentCoordinate[1]-1)
                if boardOfCharacters[left[0]][left[1]] == regionType and left in listOfCoordinatesToBeChecked:
                    listOfCoordinatesToBeChecked.remove(left)
                    region.append(left)
            except IndexError:
                pass
            try:
                right = (currentCoordinate[0], currentCoordinate[1]+1)
                if boardOfCharacters[right[0]][right[1]] == regionType and right in listOfCoordinatesToBeChecked:
                    listOfCoordinatesToBeChecked.remove(right)
                    region.append(right)
            except IndexError:
                pass
            regionIndex += 1
        listOfRegions.append(region)
    return listOfRegions

# def verticalPerimeter(region: list) -> int:
#     regionCopy = copy.deepcopy(region)
#     verticalPerimeter = 0
#     while len(regionCopy) > 0:
#         startingCoordinate = regionCopy.pop(0)
#         column = [startingCoordinate]
#         verticalPerimeter += 2
#         while len(column) > 0:
#             currentCoordinate = column.pop(0)
#             down = (currentCoordinate[0] + 1, currentCoordinate[1])
#             if down in regionCopy:
#                 regionCopy.remove(down)
#                 column.append(down)
#             up = (currentCoordinate[0] - 1, currentCoordinate[1])
#             if up in regionCopy:
#                 regionCopy.remove(up)
#                 column.append(up)
#     return verticalPerimeter
#
# def horizontalPerimeter(region: list) -> int:
#     regionCopy = copy.deepcopy(region)
#     horizontalPerimeter = 0
#     while len(regionCopy) > 0:
#         startingCoordinate = regionCopy.pop(0)
#         row = [startingCoordinate]
#         horizontalPerimeter += 2
#         while len(row) > 0:
#             currentCoordinate = row.pop(0)
#             right = (currentCoordinate[0], currentCoordinate[1] + 1)
#             if right in regionCopy:
#                 regionCopy.remove(right)
#                 row.append(right)
#             left = (currentCoordinate[0], currentCoordinate[1] - 1)
#             if left in regionCopy:
#                 regionCopy.remove(left)
#                 row.append(left)
#     return horizontalPerimeter

def part1(filename: str) -> int:
    boardOfCharacters = readFileAsBoardOfCharacters(filename)
    regions = findRegions(boardOfCharacters)
    price = 0
    for region in regions:
        regionArea = len(region)
        regionPerimeter = horizontalSides(region, True) + verticalSides(region, True)
        price += regionArea * regionPerimeter
    return price

def findUpOrDownSides(upOrDownList: list) -> int:
    verticalSides = 0
    while len(upOrDownList) > 0:
        startingCoordinate = upOrDownList.pop(0)
        row = [startingCoordinate]
        verticalSides += 1
        while len(row) > 0:
            currentCoordinate = row.pop(0)
            right = (currentCoordinate[0], currentCoordinate[1] + 1)
            if right in upOrDownList:
                upOrDownList.remove(right)
                row.append(right)
            left = (currentCoordinate[0], currentCoordinate[1] - 1)
            if left in upOrDownList:
                upOrDownList.remove(left)
                row.append(left)
    return verticalSides

def verticalSides(region: list, countAll: bool) -> int:
    regionCopy = copy.deepcopy(region)
    verticalSides = 0
    columnTops = []
    columnBottoms = []
    while len(regionCopy) > 0:
        startingCoordinate = regionCopy.pop(0)
        column = [startingCoordinate]
        columnTop = startingCoordinate[0]
        columnBottom = startingCoordinate[0]
        row = startingCoordinate[1]
        while len(column) > 0:
            currentCoordinate = column.pop(0)
            down = (currentCoordinate[0] + 1, currentCoordinate[1])
            if down in regionCopy:
                columnBottom = currentCoordinate[0] + 1
                regionCopy.remove(down)
                column.append(down)
            up = (currentCoordinate[0] - 1, currentCoordinate[1])
            if up in regionCopy:
                columnTop = currentCoordinate[0] - 1
                regionCopy.remove(up)
                column.append(up)
        columnTops.append((columnTop, row))
        columnBottoms.append((columnBottom, row))

    if countAll:
        return len(columnTops) + len(columnBottoms)

    verticalSides += findUpOrDownSides(columnTops)
    verticalSides += findUpOrDownSides(columnBottoms)

    return verticalSides

def horizontalSides(region: list, countAll: bool) -> int:
    flipRegion = []
    for coordinate in region:
        flipRegion.append((coordinate[1], coordinate[0]))
    return verticalSides(flipRegion, countAll)

# def findLeftOrRightSides(leftOrRightList: list) -> int:
#     horizontalSides = 0
#     while len(leftOrRightList) > 0:
#         startingCoordinate = leftOrRightList.pop(0)
#         column = [startingCoordinate]
#         horizontalSides += 1
#         while len(column) > 0:
#             currentCoordinate = column.pop(0)
#             down = (currentCoordinate[0] + 1, currentCoordinate[1])
#             if down in leftOrRightList:
#                 leftOrRightList.remove(down)
#                 column.append(down)
#             up = (currentCoordinate[0] - 1, currentCoordinate[1])
#             if up in leftOrRightList:
#                 leftOrRightList.remove(up)
#                 column.append(up)
#     return horizontalSides
#
# def horizontalSides(region: list, countAll: bool) -> int:
#     regionCopy = copy.deepcopy(region)
#     horizontalSides = 0
#     rowLefts = []
#     rowRights = []
#     while len(regionCopy) > 0:
#         startingCoordinate = regionCopy.pop(0)
#         row = [startingCoordinate]
#         rowLeft = startingCoordinate[1]
#         rowRight = startingCoordinate[1]
#         column = startingCoordinate[0]
#         while len(row) > 0:
#             currentCoordinate = row.pop(0)
#             left = (currentCoordinate[0], currentCoordinate[1] - 1)
#             if left in regionCopy:
#                 rowLeft = currentCoordinate[1] - 1
#                 regionCopy.remove(left)
#                 row.append(left)
#             right = (currentCoordinate[0], currentCoordinate[1] + 1)
#             if right in regionCopy:
#                 rowRight = currentCoordinate[1] + 1
#                 regionCopy.remove(right)
#                 row.append(right)
#         rowLefts.append((column, rowLeft))
#         rowRights.append((column, rowRight))
#
#     if countAll:
#         return len(rowLefts) + len(rowRights)
#
#     horizontalSides += findLeftOrRightSides(rowLefts)
#     horizontalSides += findLeftOrRightSides(rowRights)
#
#     return horizontalSides

def part2(filename: str) -> int:
    boardOfCharacters = readFileAsBoardOfCharacters(filename)
    regions = findRegions(boardOfCharacters)
    price = 0
    for region in regions:
        regionArea = len(region)
        regionPerimeter = horizontalSides(region, False) + verticalSides(region, False)
        price += regionArea * regionPerimeter
    return price

if __name__ == "__main__":
    print(part1("day12Input.txt"))
    print(part2("day12Input.txt"))