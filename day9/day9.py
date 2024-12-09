def readFileAsData(filename: str) -> (str, list):
    f = open(filename, "r")
    dataIdBlocks = []
    data = f.readlines()[0]
    for i in range(len(data)):
        if i % 2 == 0:
            dataIdBlocks.append(int(data[i]))
    f.close()
    return data, dataIdBlocks

def part1Checksum(data: str, dataIdBlocks: list) -> int:
    left = 0
    right = len(dataIdBlocks) - 1
    checksum = 0
    position = 0
    #move through the data string
    for i in range(len(data)):
        if i % 2 == 0:
            for j in range(int(data[i])):
                while dataIdBlocks[left] == 0:
                    left += 1
                    if left > len(dataIdBlocks) -1:
                        return checksum
                checksum += position * left
                position += 1
                dataIdBlocks[left] -= 1
        else:
            for j in range(int(data[i])):
                while dataIdBlocks[right] == 0:
                    right -= 1
                    if right < 0:
                        return checksum
                checksum += position * right
                position += 1
                dataIdBlocks[right] -= 1

def part2Checksum(data: str, dataIdBlocks: list) -> int:
    # empty spaces will count as 0s
    checksum = 0
    position = 0
    #move through the data string
    for i in range(len(data)):
        if dataIdBlocks == [0 for _ in range(len(dataIdBlocks))]:
            return checksum
        if i % 2 == 0:
            dataBlock = int(data[i])
            while dataBlock > 0:
                dataFoundForBlock = False
                for j in range(len(dataIdBlocks)):
                    if 1 <= dataIdBlocks[j] <= dataBlock:
                        for _ in range(dataIdBlocks[j]):
                            checksum += position * j
                            position += 1
                            dataIdBlocks[j] -= 1
                            dataBlock -= 1
                        dataFoundForBlock = True
                if dataFoundForBlock:
                    continue
                position += dataBlock
                dataBlock = 0
        else:
            dataBlock = int(data[i])
            while dataBlock > 0:
                dataFoundForBlock = False
                for j in range(1, len(dataIdBlocks)+1):
                    if 1 <= dataIdBlocks[-j] <= dataBlock:
                        for _ in range(dataIdBlocks[-j]):
                            checksum += position * (len(dataIdBlocks) - j)
                            position += 1
                            dataIdBlocks[-j] -= 1
                            dataBlock -= 1
                        dataFoundForBlock = True
                if dataFoundForBlock:
                    continue
                position += dataBlock
                dataBlock = 0
    return checksum

def part1(filename: str) -> int:
    data, dataIdBlocks = readFileAsData(filename)
    return part1Checksum(data, dataIdBlocks)

def part2(filename: str) -> int:
    data, dataIdBlocks = readFileAsData(filename)
    return part2Checksum(data, dataIdBlocks)


if __name__ == "__main__":
    print(part1("day9Input.txt"))
    print(part2("day9Input.txt"))