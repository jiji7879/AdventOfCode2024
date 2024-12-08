# list of lists
# [[1, 2, 3],
#  [4, 5, 6]]
def readFileAsBoardOfCharacters(filename: str) -> list:
    f = open(filename, "r")
    boardOfCharacters = []
    for string in f.readlines():
        boardOfCharacters.append(list(string.strip()))
    f.close()
    return boardOfCharacters

# dictionary
# Example: {"0": [(1, 9)], "a": [(8, 6), (3, 4)]}
def createDictOfFrequencies(boardOfCharacters: list) -> dict:
    dictOfFrequencies = {}
    for i in range(len(boardOfCharacters)):
        for j in range(len(boardOfCharacters[i])):
            if boardOfCharacters[i][j].isalnum():
                character = boardOfCharacters[i][j]
                if character not in dictOfFrequencies:
                    dictOfFrequencies[character] = [(i, j)]
                else:
                    dictOfFrequencies[character].append((i, j))
    return dictOfFrequencies

def findAntinodes1(boardOfCharacters: list, dictOfFrequencies: dict) -> int:
    antinodes = set()
    for value in dictOfFrequencies.values():
        for i in range(len(value)):
            for j in range(i+1, len(value)):
                try:
                    #first value is value[j], second value is value[i]
                    difference1 = (value[i][0] - value[j][0], value[i][1] - value[j][1])
                    # checks whether the coordinate is in the board
                    newXValue = value[i][0] + difference1[0]
                    newYValue = value[i][1] + difference1[1]
                    if newXValue >= 0 and newYValue >= 0:
                        _ = boardOfCharacters[newXValue][newYValue]
                        #print(newXValue, newYValue)
                        antinodes.add((newXValue, newYValue))
                except:
                    pass

                # do the same but in the opposite direction
                try:
                    # first value is value[i], second value is value[j]
                    difference1 = (value[j][0] - value[i][0], value[j][1] - value[i][1])
                    _ = boardOfCharacters[value[j][0] + difference1[0]][value[j][1] + difference1[1]]
                    newXValue = value[j][0] + difference1[0]
                    newYValue = value[j][1] + difference1[1]
                    if newXValue >= 0 and newYValue >= 0:
                        _ = boardOfCharacters[newXValue][newYValue]
                        #print(newXValue, newYValue)
                        antinodes.add((newXValue, newYValue))
                except:
                    pass
    return len(antinodes)

def findAntinodes2(boardOfCharacters: list, dictOfFrequencies: dict) -> int:
    antinodes = set()
    for value in dictOfFrequencies.values():
        for i in range(len(value)):
            for j in range(i+1, len(value)):
                antinodes.add(value[i])
                antinodes.add(value[j])
                try:
                    #first value is value[j], second value is value[i]
                    difference1 = (value[i][0] - value[j][0], value[i][1] - value[j][1])
                    newXValue = value[i][0]
                    newYValue = value[i][1]
                    pleaseBreak = False
                    while not pleaseBreak:
                        newXValue = newXValue + difference1[0]
                        newYValue = newYValue + difference1[1]
                        if newXValue >= 0 and newYValue >= 0:
                            _ = boardOfCharacters[newXValue][newYValue]
                            #print(newXValue, newYValue)
                            antinodes.add((newXValue, newYValue))
                        else:
                            pleaseBreak = True
                except:
                    pass

                # do the same but in the opposite direction
                try:
                    # first value is value[i], second value is value[j]
                    difference1 = (value[j][0] - value[i][0], value[j][1] - value[i][1])
                    _ = boardOfCharacters[value[j][0] + difference1[0]][value[j][1] + difference1[1]]
                    newXValue = value[j][0]
                    newYValue = value[j][1]
                    pleaseBreak = False
                    while not pleaseBreak:
                        newXValue = newXValue + difference1[0]
                        newYValue = newYValue + difference1[1]
                        if newXValue >= 0 and newYValue >= 0:
                            _ = boardOfCharacters[newXValue][newYValue]
                            # print(newXValue, newYValue)
                            antinodes.add((newXValue, newYValue))
                        else:
                            pleaseBreak = True
                except:
                    pass
    return len(antinodes)

def part1(filename: str) -> int:
    boardOfCharacters = readFileAsBoardOfCharacters(filename)
    dictOfFrequencies = createDictOfFrequencies(boardOfCharacters)
    return findAntinodes1(boardOfCharacters, dictOfFrequencies)

def part2(filename: str) -> int:
    boardOfCharacters = readFileAsBoardOfCharacters(filename)
    dictOfFrequencies = createDictOfFrequencies(boardOfCharacters)
    return findAntinodes2(boardOfCharacters, dictOfFrequencies)

if __name__ == "__main__":
    print(part1("day8Input.txt"))
    print(part2("day8Input.txt"))