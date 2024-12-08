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
                difference = (value[i][0] - value[j][0], value[i][1] - value[j][1])

                newXValue = value[i][0] + difference[0]
                newYValue = value[i][1] + difference[1]
                if 0 <= newXValue < len(boardOfCharacters) and 0 <= newYValue < len(boardOfCharacters[0]):
                    antinodes.add((newXValue, newYValue))

                newXValue = value[j][0] - difference[0]
                newYValue = value[j][1] - difference[1]
                if 0 <= newXValue < len(boardOfCharacters) and 0 <= newYValue < len(boardOfCharacters[0]):
                    antinodes.add((newXValue, newYValue))
    return len(antinodes)

def findAntinodes2(boardOfCharacters: list, dictOfFrequencies: dict) -> int:
    antinodes = set()
    for value in dictOfFrequencies.values():
        for i in range(len(value)):
            for j in range(i+1, len(value)):
                difference = (value[i][0] - value[j][0], value[i][1] - value[j][1])

                i1 = 0
                newXValue = value[i][0] + i1 * difference[0]
                newYValue = value[i][1] + i1 * difference[1]
                while 0 <= newXValue < len(boardOfCharacters) and 0 <= newYValue < len(boardOfCharacters[0]):
                    antinodes.add((newXValue, newYValue))
                    i1 += 1
                    newXValue = value[i][0] + i1 * difference[0]
                    newYValue = value[i][1] + i1 * difference[1]

                j1 = 0
                newXValue = value[j][0] - j1 * difference[0]
                newYValue = value[j][1] - j1 * difference[1]
                while 0 <= newXValue < len(boardOfCharacters) and 0 <= newYValue < len(boardOfCharacters[0]):
                    antinodes.add((newXValue, newYValue))
                    j1 += 1
                    newXValue = value[j][0] - j1 * difference[0]
                    newYValue = value[j][1] - j1 * difference[1]

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