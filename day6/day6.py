from enum import Enum

from numpy.f2py.auxfuncs import throw_error


class Direction(Enum):
    up = 1
    right = 2
    down = 3
    left = 4

def clockwiseTurn(direction: Direction) -> Direction:
    match direction:
        case Direction.up:
            return Direction.right
        case Direction.right:
            return Direction.down
        case Direction.down:
            return Direction.left
        case Direction.left:
            return Direction.up

# def counterClockwiseTurn(direction: Direction) -> Direction:
#     match direction:
#         case Direction.up:
#             return Direction.left
#         case Direction.right:
#             return Direction.up
#         case Direction.down:
#             return Direction.right
#         case Direction.left:
#             return Direction.down

class Guard:
    def __init__(self, map: list, starting: (int, int), direction: Direction, phantom: (int, int) = None):
        self.map = map
        self.startingPosition = starting
        self.position = starting
        self.startingDirection = direction
        self.direction = direction
        self.visitedCells = {starting}
        self.escaped = False
        self.trapped = False
        self.turnedCells = []
        self.phantom = phantom
        self.loopingCells = set()

    def nextPosition(self) -> (any, any):
        match self.direction:
            case Direction.up:
                if self.position[0]-1 < 0:
                    return "done", "done"
                else:
                    return self.position[0]-1, self.position[1]
            case Direction.right:
                if self.position[1]+1 >= len(self.map[self.position[0]]):
                    return "done", "done"
                else:
                    return self.position[0], self.position[1]+1
            case Direction.down:
                if self.position[0]+1 >= len(self.map):
                    return "done", "done"
                else:
                    return self.position[0]+1, self.position[1]
            case Direction.left:
                if self.position[1]-1 < 0:
                    return "done", "done"
                else:
                    return self.position[0], self.position[1]-1

    def move(self, phantom = None):
        if self.escaped:
            return
        nextXPosition, nextYPosition = self.nextPosition()
        if nextXPosition == "done":
            self.escaped = True
        elif (self.map[nextXPosition][nextYPosition] == '#') or (phantom == (nextXPosition, nextYPosition)):
            self.direction = clockwiseTurn(self.direction)
            # we cannot turn from the same position twice unless turning again or we're straight up trapped
            # we will usually reach the case where it's one or the other
            # the exception is if we're trapped in all sides
            if self.position in self.turnedCells and (self.turnedCells[-1] != self.position or self.turnedCells[-3::] == [self.position, self.position, self.position]):
                    self.trapped = True
            else:
                self.turnedCells.append(self.position)
        else:
            self.position = (nextXPosition, nextYPosition)
            self.visitedCells.add((nextXPosition, nextYPosition))

    def reset(self):
        self.position = self.startingPosition
        self.direction = self.startingDirection
        self.visitedCells = {self.startingPosition}
        self.escaped = False
        self.trapped = False
        self.turnedCells = []


    def escape(self) -> bool:
        self.reset()
        while not self.escaped and not self.trapped:
            self.move(self.phantom)
        return True if self.escaped else False

    def findLoops(self):
        self.reset()
        while not self.escaped and not self.trapped:
            currentPosition = self.position
            nextXPosition, nextYPosition = self.nextPosition()
            if (nextXPosition != "done" and self.map[nextXPosition][nextYPosition] != '#' and
                    (nextXPosition, nextYPosition) != self.startingPosition and (nextXPosition, nextYPosition) not in self.visitedCells):
                phantomGuard = Guard(map=self.map, starting=currentPosition, direction=self.direction, phantom=(nextXPosition, nextYPosition))
                phantomEscaped = phantomGuard.escape()
                if not phantomEscaped:
                    self.loopingCells.add((nextXPosition, nextYPosition))
            self.move()
        return True if self.escaped else False


def readInput(filename: str) -> list:
    map = []
    f = open(filename, "r")
    for line in f.readlines():
        map.append(list(line.strip()))
    f.close()
    return map

# we are assuming the direction is always up
def findStartingPosition(map: list) -> (int, int):
    for i in range(len(map)):
        for j in range(len(map[i])):
            # we are assuming the direction is always up
            if map[i][j] == '^':
                return i, j
    raise Exception("No starting position found")

def part1(filename: str) -> int:
    map = readInput(filename)
    (x, y) = findStartingPosition(map)
    guard = Guard(map, (x, y), Direction.up)
    guard.escape()
    return len(guard.visitedCells)

def part2(filename: str) -> set:
    map = readInput(filename)
    (x, y) = findStartingPosition(map)
    guard = Guard(map, (x, y), Direction.up)
    guard.findLoops()
    return guard.loopingCells


if __name__ == "__main__":
    print(part1("day6Input.txt"))
    print(len(part2("day6Input.txt")))