import re

RULE_REGEX = "(\d+)\|(\d+)"

def readInput(filename: str):
    dictOfBadPairings = {}
    listOfPageOrderings = []
    f = open(filename, "r")
    for line in f.readlines():
        matches = re.findall(RULE_REGEX, line)
        if len(matches) != 0:
            # the line looks like "#|#"
            left = int(matches[0][0])
            right = int(matches[0][1])
            addBadPairing(dictOfBadPairings, left, right)
        elif line[0].isdigit():
            # the line looks like "#,#,#,...#"
            temp = line.strip().split(",")
            rule = []
            for number in temp:
                rule.append(int(number))
            listOfPageOrderings.append(rule)
    f.close()
    return dictOfBadPairings, listOfPageOrderings

def addBadPairing(dictOfBadPairings: dict, left: int, right: int):
    if right in dictOfBadPairings:
        dictOfBadPairings[right].append(left)
    else:
        dictOfBadPairings[right] = [left]
    return dictOfBadPairings

def isGoodPageOrdering(dictOfBadPairings: dict, rule: list):
    for i in range(len(rule)):
        if rule[i] not in dictOfBadPairings:
            continue
        for j in range(i, len(rule)):
            if rule[j] in dictOfBadPairings[rule[i]]:
                return False
    return True

def fixPageOrdering(dictOfBadPairings: dict, rule: list):
    fixed = False
    while not fixed:
        didStep = False
        for i in range(len(rule)):
            if rule[i] not in dictOfBadPairings:
                continue
            for j in range(i, len(rule)):
                if rule[j] in dictOfBadPairings[rule[i]]:
                    page = rule.pop(j)
                    rule.insert(i, page)
                    didStep = True
                    break
        if not didStep:
            fixed = True
    return rule


def part1(filename: str):
    dictOfBadPairings, listOfRules = readInput(filename)
    sumOfMiddlePages = 0
    for rule in listOfRules:
        if isGoodPageOrdering(dictOfBadPairings, rule):
            #assuming an odd page number
            sumOfMiddlePages += rule[len(rule)//2]
    return sumOfMiddlePages

def part2(filename: str):
    dictOfBadPairings, listOfRules = readInput(filename)
    sumOfMiddlePages = 0
    for rule in listOfRules:
        if not isGoodPageOrdering(dictOfBadPairings, rule):
            newRule = fixPageOrdering(dictOfBadPairings, rule)
            # assuming an odd page number
            sumOfMiddlePages += newRule[len(newRule) // 2]
    return sumOfMiddlePages

if __name__ == "__main__":
    print(part1("day5Input.txt"))
    print(part2("day5Input.txt"))
