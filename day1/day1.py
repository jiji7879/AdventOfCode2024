#From the Advent of Code website for testing


def makeLists():
    f = open("day1Input.txt", "r")
    leftList = []
    rightList = []
    for line in f.readlines():
        line.strip()
        numberSplit = line.split()  # splits into left and right
        leftList.append(int(numberSplit[0]))
        rightList.append(int(numberSplit[1]))
    f.close()

    return leftList, rightList

def part1(leftList: list, rightList: list):
    leftList.sort()
    rightList.sort()

    total = 0
    for i in range(len(leftList)):
        total += abs(leftList[i] - rightList[i])
    return total

#seems inefficient for larger sets, but gets the job done
def part2(leftList: list, rightList: list):
    total = 0
    for i in leftList:
        j = rightList.count(i)
        total += i * j
    return total

if __name__ == "__main__":
    leftList, rightList = makeLists()
    print(part1(leftList, rightList))
    print(part2(leftList, rightList))