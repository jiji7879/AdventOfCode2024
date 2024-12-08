import copy

def readFileAsArrayOfEquations(filename: str) -> list:
    f = open(filename, "r")
    arrayOfEquations = []
    for equation in f.readlines():
        equationList = equation.strip().split()
        equationList[0] = equationList[0][:-1]
        newEquationList = []
        for number in equationList:
            newEquationList.append(int(number))
        arrayOfEquations.append(newEquationList)
    f.close()
    return arrayOfEquations

def checkEquation(equationLine: list, checkContatination: bool) -> bool:
    result = False
    while not result:
        #basic checks
        if len(equationLine) == 1:
            return True if equationLine[0] == 0 else False
        elif len(equationLine) == 2:
            return True if equationLine[0] == equationLine[1] else False
        elif len(equationLine) == 3:
            if (equationLine[0] == equationLine[1] + equationLine[2] or
                    equationLine[0] == equationLine[1] * equationLine[2] or
                    (checkContatination and str(equationLine[0]) == str(equationLine[1]) + str(equationLine[2]))):
                return True
            else:
                return False

        #check multiply
        if equationLine[0] % equationLine[-1] == 0:
            newMultiplyEquationLine = equationLine[:-1]
            newMultiplyEquationLine[0] = equationLine[0] // equationLine[-1]
            multiplyCheck = checkEquation(newMultiplyEquationLine, checkContatination)
            if multiplyCheck:
                return True

        #check concatination
        if checkContatination:
            total = str(equationLine[0])
            lastPart = str(equationLine[-1])
            totalFirstPartLength = len(total) - len(lastPart)
            firstPart = total[0:totalFirstPartLength]
            if firstPart + lastPart == total:
                newConcatEquationLine = equationLine[:-1]
                try:
                    newConcatEquationLine[0] = int(firstPart)
                except:
                    newConcatEquationLine[0] = 0
                concatinationCheck = checkEquation(newConcatEquationLine, checkContatination)
                if concatinationCheck:
                    return True

        equationLine[0] = equationLine[0] - equationLine[-1]
        equationLine.pop(-1)

def checkArrayOfEquations(arrayOfEquations: list, checkConcatination: bool) -> int:
    total = 0
    for equation in arrayOfEquations:
        equationCopy = copy.deepcopy(equation)
        if checkEquation(equationCopy, checkConcatination):
            total += equation[0]
    return total

if __name__ == "__main__":
    arrayOfEquations = readFileAsArrayOfEquations("day7Input.txt")
    print(checkArrayOfEquations(arrayOfEquations, False))
    print(checkArrayOfEquations(arrayOfEquations, True))