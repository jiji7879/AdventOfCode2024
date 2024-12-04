import wordSearch

XMAS_STRING = "XMAS"
MAS_STRING = "MAS"

def readFileAsArrayOfCharacters(filename: str):
    f = open(filename, "r")
    arrayOfCharacters = []
    for string in f.readlines():
        arrayOfCharacters.append(list(string.strip()))
    f.close()
    return arrayOfCharacters

def part1(filename: str):
    array = readFileAsArrayOfCharacters(filename)
    return wordSearch.wordSearch(array, XMAS_STRING)

def part2(filename: str):
    array = readFileAsArrayOfCharacters(filename)

    counter = 0
    numRows = len(array)
    numColumns = len(array[0])

    # checks if the created string is the same as the search string.
    # note that searchString[::-1] reverses the string.

    for i in range(1, numRows - 1):
        for j in range(1, numColumns - 1):
            has_diagonal_left = False

            #diagonal-right
            created_string = ""
            for k in range(-1, 2):
                created_string += array[i + k][j + k]
            #skip if a diagonal-right match is not found
            if not (created_string == MAS_STRING or created_string == MAS_STRING[::-1]):
                continue

            #diagonal-left
            created_string = ""
            for k in range(-1, 2):
                created_string += array[i - k][j + k]
            #add to the counter if a diagonal-left match is found
            if created_string == MAS_STRING or created_string == MAS_STRING[::-1]:
                counter += 1

    return counter

if __name__ == "__main__":
    print(part1("day4Input.txt"))
    print(part2("day4Input.txt"))