import functools
import math

def temp_log_10(number: int) -> float:
    if number <= 0:
        return -1
    return math.log10(number)

def number_of_digits(number: int) -> int:
    count = 0
    while number != 0:
        count += 1
        number /= 10
    return count

@functools.lru_cache(None)
def blink_action(num: int) -> list:
    if num == 0:
        return [1]
    if len(str(num)) % 2 == 0:
        firstPart = int(str(num)[:len(str(num))//2])
        lastPart = int(str(num)[len(str(num))//2:])
        return [firstPart, lastPart]
    return [num * 2024]

def blink_multiple_times(initialList: list, times: int) -> list:
    for j in range(times):
        new_list = []
        i = 0
        while i < len(initialList):
            blinkAction1 = blink_action(initialList[i])
            new_list += blinkAction1
            i += 1
        initialList = new_list
    return initialList

def part1(initialList: list, times: int) -> int:
    return len(blink_multiple_times(initialList, times))

@functools.lru_cache(None)
def blink_action_count(blinkInt: int, count: int) -> int:
    if count == 0:
        return 1
    if blinkInt == 0:
        return blink_action_count(1, count - 1)
    if len(str(blinkInt)) % 2 == 0:
        firstPart = int(str(blinkInt)[:len(str(blinkInt)) // 2])
        lastPart = int(str(blinkInt)[len(str(blinkInt)) // 2:])
        return blink_action_count(firstPart, count - 1) + blink_action_count(lastPart, count - 1)
    return blink_action_count(blinkInt * 2024, count - 1)

def part2(initialList: list, times: int) -> int:
    count = 0
    for num in initialList:
        count += blink_action_count(num, times)
    return count

if __name__ == "__main__":
    print(part2([4, 4841539, 66, 5279, 49207, 134, 609568, 0], 25))
    print(part2([4, 4841539, 66, 5279, 49207, 134, 609568, 0], 75))