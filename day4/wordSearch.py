def wordSearch(array: list, searchString: str):

    counter = 0
    numRows = len(array)
    numColumns = len(array[0])

    #checks if the created string is the same as the search string.
    #note that searchString[::-1] reverses the string.

    # horizontal
    for i in range(numRows):
        for j in range(numColumns - (len(searchString) - 1)):
            created_string = ""
            for k in range(0, len(searchString)):
                created_string += array[i][j + k]
            if created_string == searchString or created_string == searchString[::-1]:
                counter += 1

    # vertical
    for i in range(numRows - (len(searchString) - 1)):
        for j in range(numColumns):
            created_string = ""
            for k in range(0, len(searchString)):
                created_string += array[i + k][j]
            if created_string == searchString or created_string == searchString[::-1]:
                counter += 1

    # diagonal-right
    for i in range(numRows - (len(searchString) - 1)):
        for j in range(numColumns - (len(searchString) - 1)):
            created_string = ""
            for k in range(0, len(searchString)):
                created_string += array[i + k][j + k]
            if created_string == searchString or created_string == searchString[::-1]:
                counter += 1

    # diagonal-left
    for i in range((len(searchString) - 1), numRows):
        for j in range(numColumns - (len(searchString) - 1)):
            created_string = ""
            for k in range(0, len(searchString)):
                created_string += array[i - k][j + k]
            if created_string == searchString or created_string == searchString[::-1]:
                counter += 1

    return counter