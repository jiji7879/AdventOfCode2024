import math
import re
from PIL import Image

ROBOT_REGEX = "p=(-?\d+),(-?\d+) v=(-?\d+),(-?\d+)"
def readFileAsRobots(filename: str) -> (list, list):
    f = open(filename, "r")
    robotPositions = []
    robotVelocities = []
    for line in f.readlines():
        robotMatches = re.findall(ROBOT_REGEX, line)
        if robotMatches is not None:
            match = robotMatches[0]
            robotPositions.append([int(match[0]), int(match[1])])
            robotVelocities.append([int(match[2]), int(match[3])])
        else:
            print("Error!")
    f.close()
    return robotPositions, robotVelocities

#robotList takes in a list of robots with 2 things in its list:
#The first is its position
#The second is its velocity vector
def predictFinalQuadrant(robotPositions: list, robotVelocities: list, boardWidth: int, boardHeight: int, numMoves: int) -> list:
    if len(robotPositions) != len(robotVelocities):
        return []
    finalRobotQuadrants = [0, 0, 0, 0]
    for index in range(len(robotPositions)):
        initialPosition = robotPositions[index]
        velocity = robotVelocities[index]
        finalHorizontal = (initialPosition[0] + velocity[0] * numMoves) % boardWidth
        finalVertical = (initialPosition[1] + velocity[1] * numMoves) % boardHeight
        if finalHorizontal < boardWidth // 2:
            if finalVertical < boardHeight // 2:
                finalRobotQuadrants[0] += 1
            elif finalVertical >= math.ceil(boardHeight / 2):
                finalRobotQuadrants[1] += 1
        elif finalHorizontal >= math.ceil(boardWidth / 2):
            if finalVertical < boardHeight // 2:
                finalRobotQuadrants[2] += 1
            elif finalVertical >= math.ceil(boardHeight / 2):
                finalRobotQuadrants[3] += 1
    return finalRobotQuadrants

def part1(filename: str, boardWidth: int, boardHeight: int, numMoves: int) -> int:
    robotPositions, robotVelocities = readFileAsRobots(filename)
    quadrants = predictFinalQuadrant(robotPositions, robotVelocities, boardWidth, boardHeight, numMoves)
    product = 1
    for i in quadrants:
        product *= i
    return product

def move(robotPositions: list, robotVelocities: list, boardWidth: int, boardHeight: int):
    finalRobotPositions = []
    for index in range(len(robotPositions)):
        initialPosition = robotPositions[index]
        velocity = robotVelocities[index]
        finalHorizontal = (initialPosition[0] + velocity[0]) % boardWidth
        finalVertical = (initialPosition[1] + velocity[1]) % boardHeight
        finalRobotPositions.append([finalHorizontal, finalVertical])
    return finalRobotPositions

#note that it will cycle through after boardWidth * boardHeight number of moves
def part2(filename: str, boardWidth: int, boardHeight: int, numMoves: int):
    robotPositions, robotVelocities = readFileAsRobots(filename)

    for imageNumber in range(max(boardWidth * boardHeight, numMoves)):
        image = Image.new("1", (boardWidth, boardHeight))
        pixels = image.load()
        for position in robotPositions:
            pixels[position[0], position[1]] = 1
        image_path = f"images\\{imageNumber}.png"
        image.save(image_path)
        #move at the end
        robotPositions = move(robotPositions, robotVelocities, boardWidth, boardHeight)

if __name__ == "__main__":
    print(part1("day14Input.txt", 101, 103, 100))
    part2("day14Input.txt", 101, 103, 10403)