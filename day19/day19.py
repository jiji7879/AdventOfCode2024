import functools


def readTowelPatterns(filename: str) -> (dict, list):
    f = open(filename, "r")
    dictOfPatterns = {"w": [], "u": [], "b": [], "r": [], "g": []}
    goalList = []
    # we assume the input is absolutely correct
    lines = f.readlines()
    for i in range(len(lines)):
        if i == 0:
            line = lines[i]
            patterns = line.strip().split(", ")
            for pattern in patterns:
                dictOfPatterns[pattern[0]].append(pattern)
        else:
            line = lines[i]
            line = line.strip()
            if line != "":
                goalList.append(line)
    f.close()
    return dictOfPatterns, goalList


def checkGoal(dictOfPatterns, goal) -> int:
    if goal == "" or goal[0] not in dictOfPatterns:
        return 0
    for pattern in dictOfPatterns[goal[0]]:
        if pattern == goal:
            return 1
        if goal[0:len(pattern)] == pattern and checkGoal(dictOfPatterns, goal[len(pattern):]):
            return 1
    return 0


def part1(filename: str) -> int:
    dictOfPatterns, goalList = readTowelPatterns(filename)
    goalsAchieved = 0
    for goal in goalList:
        goalsAchieved += checkGoal(dictOfPatterns, goal)
    return goalsAchieved


def part2(filename: str) -> int:
    dictOfPatterns, goalList = readTowelPatterns(filename)
    goalsAchieved = 0

    # we're going to cache the checkGoals2 function
    # unfortunatley we need all the arguments to be hashable
    # dicts and lists are not hashable, since they are mutable.
    # Thus, we can use either frozensets or tuples, and then recreate the dictionary if needed
    for item in dictOfPatterns.keys():
        value = tuple(dictOfPatterns[item])
        dictOfPatterns[item] = value
    patternTuples = tuple(dictOfPatterns.items())

    for goal in goalList:
        goalsAchieved += checkGoal2(patternTuples, goal)
    return goalsAchieved


def recreateDictOfPatterns(patternTuples: tuple) -> dict:
    dictOfPatterns = {}
    for x in patternTuples:
        value = []
        for y in x[1]:
            value.append(y)
        dictOfPatterns[x[0]] = value
    return dictOfPatterns


@functools.lru_cache(None)
def checkGoal2(patternTuples: tuple, goal: str) -> int:
    dictOfPatterns = recreateDictOfPatterns(patternTuples)
    if goal == "" or goal[0] not in dictOfPatterns:
        return 0
    num = 0
    for pattern in dictOfPatterns[goal[0]]:
        if pattern == goal:
            num += 1
        if goal[0:len(pattern)] == pattern:
            num += checkGoal2(patternTuples, goal[len(pattern):])
    return num


if __name__ == "__main__":
    print(part1("day19Input.txt"))
    print(part2("day19Input.txt"))
