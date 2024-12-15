import re

WALL_ROBOT_BOXES_REGEX = "[O.#]+"
MOVE_REGEX = "[\^v<>]+"


def readRobotInputs1(filename: str):
    f = open(filename, "r")
    walls = set()
    robots = []
    boxes = []
    moveMatches = []
    # we assume the input is absolutely correct
    lines = f.readlines()
    for i in range(len(lines)):
        line = lines[i]
        line = line.strip()
        wallRobotBoxesMatch = re.findall(WALL_ROBOT_BOXES_REGEX, line)
        moveMatch = re.findall(MOVE_REGEX, line)
        if len(wallRobotBoxesMatch) > 0:
            boardLine = list(line)
            for j in range(len(boardLine)):
                if boardLine[j] == 'O':
                    boxes.append((i, j))
                elif boardLine[j] == '#':
                    walls.add((i, j))
                elif boardLine[j] == '@':
                    robots.append((i, j))
        elif len(moveMatch) > 0:
            moves = list(line)
            for move in moves:
                moveMatches.append(move)
    f.close()
    return [walls, robots, boxes, moveMatches]


def moveRobot1(walls: set, robots: list, boxes: list, moveMatches: list) -> (list, list):
    for move in moveMatches:
        if move == '^':
            new_robot_height = robots[0][0] - 1
            new_robot_width = robots[0][1]
            if (new_robot_height, new_robot_width) not in walls and (new_robot_height, new_robot_width) not in boxes:
                robots[0] = (new_robot_height, new_robot_width)
                continue
            if (new_robot_height, new_robot_width) in walls:
                continue
            elif (new_robot_height, new_robot_width) in boxes:
                k = 2
                while (robots[0][0] - k, robots[0][1]) in boxes:
                    k += 1
                if (robots[0][0] - k, robots[0][1]) in walls:
                    continue
                else:
                    boxes.remove((new_robot_height, new_robot_width))
                    boxes.append((robots[0][0] - k, robots[0][1]))
                    robots[0] = (new_robot_height, new_robot_width)
        elif move == '<':
            new_robot_height = robots[0][0]
            new_robot_width = robots[0][1] - 1
            if (new_robot_height, new_robot_width) not in walls and (new_robot_height, new_robot_width) not in boxes:
                robots[0] = (new_robot_height, new_robot_width)
                continue
            if (new_robot_height, new_robot_width) in walls:
                continue
            elif (new_robot_height, new_robot_width) in boxes:
                k = 2
                while (robots[0][0], robots[0][1] - k) in boxes:
                    k += 1
                if (robots[0][0], robots[0][1] - k) in walls:
                    continue
                else:
                    boxes.remove((new_robot_height, new_robot_width))
                    boxes.append((robots[0][0], robots[0][1] - k))
                    robots[0] = (new_robot_height, new_robot_width)
        elif move == '>':
            new_robot_height = robots[0][0]
            new_robot_width = robots[0][1] + 1
            if (new_robot_height, new_robot_width) not in walls and (new_robot_height, new_robot_width) not in boxes:
                robots[0] = (new_robot_height, new_robot_width)
                continue
            if (new_robot_height, new_robot_width) in walls:
                continue
            elif (new_robot_height, new_robot_width) in boxes:
                k = 2
                while (robots[0][0], robots[0][1] + k) in boxes:
                    k += 1
                if (robots[0][0], robots[0][1] + k) in walls:
                    continue
                else:
                    boxes.remove((new_robot_height, new_robot_width))
                    boxes.append((robots[0][0], robots[0][1] + k))
                    robots[0] = (new_robot_height, new_robot_width)
        elif move == 'v':
            new_robot_height = robots[0][0] + 1
            new_robot_width = robots[0][1]
            if (new_robot_height, new_robot_width) not in walls and (new_robot_height, new_robot_width) not in boxes:
                robots[0] = (new_robot_height, new_robot_width)
                continue
            if (new_robot_height, new_robot_width) in walls:
                continue
            elif (new_robot_height, new_robot_width) in boxes:
                k = 2
                while (robots[0][0] + k, robots[0][1]) in boxes:
                    k += 1
                if (robots[0][0] + k, robots[0][1]) in walls:
                    continue
                else:
                    boxes.remove((new_robot_height, new_robot_width))
                    boxes.append((robots[0][0] + k, robots[0][1]))
                    robots[0] = (new_robot_height, new_robot_width)
    return robots, boxes


def part1(filename: str) -> int:
    robotLists = readRobotInputs1(filename)
    newRobotCoordinates, newBoxCoordinates = moveRobot1(robotLists[0], robotLists[1], robotLists[2], robotLists[3])
    gps = 0
    for box in newBoxCoordinates:
        gps += box[0] * 100 + box[1]
    return gps


def readRobotInputs2(filename: str):
    f = open(filename, "r")
    walls = set()
    robots = []
    boxes = list()
    moveMatches = []
    # we assume the input is absolutely correct
    lines = f.readlines()
    for i in range(len(lines)):
        line = lines[i]
        line = line.strip()
        wallRobotBoxesMatch = re.findall(WALL_ROBOT_BOXES_REGEX, line)
        moveMatch = re.findall(MOVE_REGEX, line)
        if len(wallRobotBoxesMatch) > 0:
            boardLine = list(line)
            for j in range(len(boardLine)):
                if boardLine[j] == 'O':
                    boxes.append((i, 2 * j))
                elif boardLine[j] == '#':
                    walls.add((i, 2 * j))
                elif boardLine[j] == '@':
                    robots.append((i, 2 * j))
        elif len(moveMatch) > 0:
            moves = list(line)
            for move in moves:
                moveMatches.append(move)
    f.close()
    return [walls, robots, boxes, moveMatches]


def findAllMovingBoxes(movingBox: (int, int), walls: set, boxes: list, move: str) -> list:
    if move == '^':
        newHeight = movingBox[0] - 1
    else:
        newHeight = movingBox[0] + 1
    if (newHeight, movingBox[1]) in walls or (newHeight, movingBox[1] - 1) in walls or (
    newHeight, movingBox[1] + 1) in walls:
        return [-1]
    affected_boxes = [movingBox]
    if (newHeight, movingBox[1] - 1) in boxes:
        x = findAllMovingBoxes((newHeight, movingBox[1] - 1), walls, boxes, move)
        if x == [-1]:
            return [-1]
        affected_boxes += x
    if (newHeight, movingBox[1]) in boxes:
        x = findAllMovingBoxes((newHeight, movingBox[1]), walls, boxes, move)
        if x == [-1]:
            return [-1]
        affected_boxes += x
    if (newHeight, movingBox[1] + 1) in boxes:
        x = findAllMovingBoxes((newHeight, movingBox[1] + 1), walls, boxes, move)
        if x == [-1]:
            return [-1]
        affected_boxes += x
    affected_boxes = list(set(affected_boxes))
    return affected_boxes


def moveRobot2(walls: set, robots: list, boxes: list, moveMatches: list) -> (list, set):
    for move in moveMatches:
        if move == '^':
            new_robot_height = robots[0][0] - 1
            new_robot_width = robots[0][1]
            if (((new_robot_height, new_robot_width) not in walls and (
            new_robot_height, new_robot_width - 1) not in walls) and
                    ((new_robot_height, new_robot_width) not in boxes and (
                    new_robot_height, new_robot_width - 1) not in boxes)):
                robots[0] = (new_robot_height, new_robot_width)
                continue
            if (new_robot_height, new_robot_width) in walls or (new_robot_height, new_robot_width - 1) in walls:
                continue
            elif (new_robot_height, new_robot_width) in boxes:
                affected_boxes = findAllMovingBoxes((new_robot_height, new_robot_width), walls, boxes, move)
                if affected_boxes == [-1]:
                    continue
                else:
                    robots[0] = (new_robot_height, new_robot_width)
                    for box in affected_boxes:
                        boxes.remove((box[0], box[1]))
                        boxes.append((box[0] - 1, box[1]))
            elif (new_robot_height, new_robot_width - 1) in boxes:
                affected_boxes = findAllMovingBoxes((new_robot_height, new_robot_width - 1), walls, boxes, move)
                if affected_boxes == [-1]:
                    continue
                else:
                    robots[0] = (new_robot_height, new_robot_width)
                    for box in affected_boxes:
                        boxes.remove((box[0], box[1]))
                        boxes.append((box[0] - 1, box[1]))
        elif move == '<':
            new_robot_height = robots[0][0]
            new_robot_width = robots[0][1] - 1
            if (new_robot_height, new_robot_width - 1) not in walls and (
            new_robot_height, new_robot_width - 1) not in boxes:
                robots[0] = (new_robot_height, new_robot_width)
                continue
            if (new_robot_height, new_robot_width - 1) in walls:
                continue
            elif (new_robot_height, new_robot_width - 1) in boxes:
                k = 2
                while (new_robot_height, new_robot_width - k - 1) in boxes:
                    k += 2
                if (new_robot_height, new_robot_width - k - 1) in walls:
                    continue
                else:
                    for i in range(0, k, 2):
                        boxes.remove((new_robot_height, new_robot_width - i - 1))
                        boxes.append((new_robot_height, new_robot_width - i - 2))
                    robots[0] = (new_robot_height, new_robot_width)
        elif move == '>':
            new_robot_height = robots[0][0]
            new_robot_width = robots[0][1] + 1
            if (new_robot_height, new_robot_width) not in walls and (
                    new_robot_height, new_robot_width) not in boxes:
                robots[0] = (new_robot_height, new_robot_width)
                continue
            if (new_robot_height, new_robot_width) in walls:
                continue
            elif (new_robot_height, new_robot_width) in boxes:
                k = 2
                while (new_robot_height, new_robot_width + k) in boxes:
                    k += 2
                if (new_robot_height, new_robot_width + k) in walls:
                    continue
                else:
                    for i in range(0, k, 2):
                        boxes.remove((new_robot_height, new_robot_width + i))
                        boxes.append((new_robot_height, new_robot_width + i + 1))
                    robots[0] = (new_robot_height, new_robot_width)
        elif move == 'v':
            new_robot_height = robots[0][0] + 1
            new_robot_width = robots[0][1]
            if (((new_robot_height, new_robot_width) not in walls and (
            new_robot_height, new_robot_width - 1) not in walls) and
                    ((new_robot_height, new_robot_width) not in boxes and (
                    new_robot_height, new_robot_width - 1) not in boxes)):
                robots[0] = (new_robot_height, new_robot_width)
                continue
            if (new_robot_height, new_robot_width) in walls or (new_robot_height, new_robot_width - 1) in walls:
                continue
            elif (new_robot_height, new_robot_width) in boxes:
                affected_boxes = findAllMovingBoxes((new_robot_height, new_robot_width), walls, boxes, move)
                if affected_boxes == [-1]:
                    continue
                else:
                    robots[0] = (new_robot_height, new_robot_width)
                    for box in affected_boxes:
                        boxes.remove((box[0], box[1]))
                        boxes.append((box[0] + 1, box[1]))
            elif (new_robot_height, new_robot_width - 1) in boxes:
                affected_boxes = findAllMovingBoxes((new_robot_height, new_robot_width - 1), walls, boxes, move)
                if affected_boxes == [-1]:
                    continue
                else:
                    robots[0] = (new_robot_height, new_robot_width)
                    for box in affected_boxes:
                        boxes.remove((box[0], box[1]))
                        boxes.append((box[0] + 1, box[1]))
    return robots, boxes


def part2(filename: str) -> int:
    robotLists = readRobotInputs2(filename)
    newRobotCoordinates, newBoxCoordinates = moveRobot2(robotLists[0], robotLists[1], robotLists[2], robotLists[3])
    gps = 0
    for box in newBoxCoordinates:
        gps += box[0] * 100 + box[1]
    return gps


if __name__ == "__main__":
    print(part1("day15Input.txt"))
    print(part2("day15Input.txt"))
