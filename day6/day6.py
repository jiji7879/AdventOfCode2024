from enum import Enum

class Direction(Enum):
    up = 1
    right = 2
    down = 3
    left = 4

def clockwiseTurn(direction: Direction) -> Direction:
