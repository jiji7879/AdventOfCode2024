import re
from collections import defaultdict

NETWORK_REGEX = "(.+)-(.+)"


def readNetwork(filename: str) -> dict[str, set]:
    f = open(filename, "r")
    network = defaultdict(set)
    # we assume the input is absolutely correct
    for line in f.readlines():
        networkMatch = re.findall(NETWORK_REGEX, line)
        if networkMatch is not None:
            network[networkMatch[0][0]].add(networkMatch[0][1])
            network[networkMatch[0][1]].add(networkMatch[0][0])
        else:
            print("Error!")
    f.close()
    return network


def findTriangleWithTStart(network: dict[str, set]) -> int:
    count = 0
    three_count = 0
    for node1 in network.keys():
        if node1[0] != "t":
            continue
        for node2 in network[node1]:
            # note for a network with 2 ts, the "else" will count twice. t1 -> o -> t2, and t2 -> o -> t1. Then we divide by 2.
            # for a network with 3 ts, we have t1 -> t2 -> t3, t1 -> t3 -> t2, and 4 other variations starting with t2 and t3. We then divide by 6.
            if node2[0] == "t":
                intersection = network[node2].intersection(network[node1])
                for node3 in intersection:
                    if node3[0] == "t":
                        three_count += 1
            else:
                count += len(network[node2].intersection(network[node1]))
    return count // 2 + three_count // 6


def part1(filename: str) -> int:
    network = readNetwork(filename)
    return findTriangleWithTStart(network)


def findBiggestParty(network: dict[str, set]):
    oldBiggestParty = dict()
    for node1 in network:
        for node2 in network[node1]:
            intersection = network[node2].intersection(network[node1])
            for node3 in intersection:
                listOfNodes = [node1, node2, node3]
                listOfNodes.sort()
                if tuple(listOfNodes) not in oldBiggestParty:
                    oldBiggestParty[tuple(listOfNodes)] = network[node3].intersection(intersection)
    while len(oldBiggestParty) > 1:
        newBiggestParty = dict()
        for partyNetwork in oldBiggestParty:
            if len(oldBiggestParty[partyNetwork]) == 0:
                continue
            isection = network[partyNetwork[0]]
            for computer in partyNetwork:
                isection = isection.intersection(network[computer])
            for newNode in oldBiggestParty[partyNetwork]:
                listOfNodes = list(partyNetwork)
                listOfNodes.append(newNode)
                listOfNodes.sort()
                if tuple(listOfNodes) not in newBiggestParty:
                    newBiggestParty[tuple(listOfNodes)] = network[newNode].intersection(isection)
        oldBiggestParty = newBiggestParty
    return oldBiggestParty


def part2(filename: str):
    network = readNetwork(filename)
    party = findBiggestParty(network)
    string = ""
    for party in party.keys():
        string = ""
        for computer in party:
            string += computer + ","
    return string[:-1]


if __name__ == "__main__":
    print(part1("day23Input.txt"))
    print(part2("day23Input.txt"))
