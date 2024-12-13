import re
import math

BUTTON_A_REGEX = "Button A\: X\+(\d+), Y\+(\d+)"
BUTTON_B_REGEX = "Button B\: X\+(\d+), Y\+(\d+)"
PRIZE_REGEX = "Prize\: X=(\d+), Y=(\d+)"

def find_slope(coordinate: (int, int)) -> float:
    if coordinate[0] == 0:
        slope = math.inf
    else:
        slope = coordinate[1]/coordinate[0]
    return slope

#assuming buttonA and buttonB have the same slope
def find_same_slope_optimal(buttonA: (int, int), buttonB: (int, int), prize: (int, int)) -> int:
    if buttonA[0] >= 3 * buttonB[0]:
        buttonBPress = 0
        newPrize = (prize[0], prize[1])
        while newPrize[0] >= 0:
            if newPrize[0] % buttonA[0] == 0:
                return newPrize[0] // buttonA[0] * 3 + buttonBPress
            newPrize[0] -= buttonB[0]
            newPrize[1] -= buttonB[1]
            buttonBPress += 1
        return 0
    else:
        buttonAPress = 0
        newPrize = (prize[0], prize[1])
        while newPrize[0] >= 0:
            if newPrize[0] % buttonB[0] == 0:
                return newPrize[0] // buttonB[0] + buttonAPress * 3
            newPrize[0] -= buttonA[0]
            newPrize[1] -= buttonA[1]
            buttonAPress += 1
        return 0

#small button has smaller slope than bigButton
# def find_presses_to_solution(smallButton: (int, int), bigButton: (int, int), prize: (int, int)) -> list:
#     currentCoordinate = [smallButton[0], smallButton[1]]
#     currentScore = [1, 0]
#     prizeSlope = prize[1]/prize[0]
#
#     while currentCoordinate[0] != prize[0] or currentCoordinate[1] != prize[1]:
#         if currentCoordinate[0] > prize[0]:
#             return [0, 0]
#         if currentCoordinate[1] * prize[0] < prize[1] * currentCoordinate[0]:
#             currentCoordinate[1] += bigButton[1]
#             currentCoordinate[0] += bigButton[0]
#             currentScore[1] += 1
#         elif currentCoordinate[1] * prize[0] > prize[1] * currentCoordinate[0]:
#             currentCoordinate[1] += smallButton[1]
#             currentCoordinate[0] += smallButton[0]
#             currentScore[0] += 1
#         # if the slopes are the same, there's no other way of getting to this point.
#         else:
#             if prize[0] % currentCoordinate[0] == 0:
#                 multiplier = prize[0] // currentCoordinate[0]
#                 currentScore[0] *= multiplier
#                 currentScore[1] *= multiplier
#                 return currentScore
#             else:
#                 return [0, 0]
#     return currentScore

def find_two_button_solution(buttonA: (int, int), buttonB: (int, int), prize: (int, int)) -> int:
    buttonASlope = find_slope(buttonA)
    buttonBSlope = find_slope(buttonB)
    prizeSlope = find_slope(prize)

    if prizeSlope > buttonASlope and prizeSlope > buttonBSlope:
        return 0
    elif prizeSlope < buttonASlope and prizeSlope < buttonBSlope:
        return 0

    if prizeSlope == buttonASlope and prizeSlope != buttonBSlope:
        return prize[0]//buttonA[0] * 3 if prize[0] % buttonA[0] == 0 else 0
    elif prizeSlope == buttonBSlope and prizeSlope != buttonASlope:
        return prize[0]//buttonB[0] if prize[0] % buttonB[0] == 0 else 0
    elif prizeSlope == buttonASlope and prizeSlope == buttonBSlope:
        return find_same_slope_optimal(buttonA, buttonB, prize)

    if buttonASlope < buttonBSlope:
        score = find_presses_to_solution(buttonA, buttonB, prize)
        return score[0] * 3 + score[1]
    else:
        score = find_presses_to_solution(buttonB, buttonA, prize)
        return score[1] * 3 + score[0]

def part1(filename: str) -> int:
    f = open(filename, "r")
    lines = f.readlines()
    tokenCount = 0
    #we assume the input is absolutely correct
    for i in range(0, len(lines)+1, 4):
        buttonAMatches = re.findall(BUTTON_A_REGEX, lines[i])
        buttonA = (int(buttonAMatches[0][0]), int(buttonAMatches[0][1]))
        buttonBMatches = re.findall(BUTTON_B_REGEX, lines[i+1])
        buttonB = (int(buttonBMatches[0][0]), int(buttonBMatches[0][1]))
        prizeMatches = re.findall(PRIZE_REGEX, lines[i+2])
        prize = (int(prizeMatches[0][0]), int(prizeMatches[0][1]))
        tokenCount += find_two_button_solution(buttonA, buttonB, prize)
    f.close()
    return tokenCount

#Let button A have slopes (A1, A2)
#Let button B have slopes (B1, B2)
#Let prize have coordinate (P1, P2)
#Assume that A and B have different slopes
#Then the order of pressing A and B doesn't matter. All that matters is that it's pressed the correct number of ways.
#It's easy to press all As then all Bs.
#All As since the start will look like the equation y = A2/A1 x
#All Bs until the prize will look like the equation y-P2 = B2/B1 (x-P1) so y = B2/B1 (x-P1) + P2
#So we need the x solution when A2/A1 x = B2/B1 (x-P1) + P2
# A2/A1 x = B2/B1 x - P1 * (B2/B1) + P2
# (A2 * B1 - B2 * A1)/(A1 * B1) x = P2 - P1 * (B2/B1)
# x = (P2 - P1 * B2/B1)(A1 * B1)/(A2 * B1 - B2 * A1)
# x = (P2 * B1 - P1 * B2)(A1)/(A2 * B1 - B2 * A1)

def find_presses_to_solution(smallButton: (int, int), bigButton: (int, int), prize: (int, int)) -> list:
    if (prize[1] * bigButton[0] - prize[0] * bigButton[1]) * (smallButton[0]) % (smallButton[1] * bigButton[0] - bigButton[1] * smallButton[0]) != 0:
        return [0, 0]
    x_coordinate_meet = (prize[1] * bigButton[0] - prize[0] * bigButton[1]) * (smallButton[0])//(smallButton[1] * bigButton[0] - bigButton[1] * smallButton[0])
    if x_coordinate_meet % smallButton[0] != 0 or (prize[0] - x_coordinate_meet) % bigButton[0] != 0:
        return [0, 0]
    else:
        return [x_coordinate_meet // smallButton[0], (prize[0] - x_coordinate_meet) // bigButton[0]]

def part2(filename: str) -> int:
    f = open(filename, "r")
    lines = f.readlines()
    tokenCount = 0
    #we assume the input is absolutely correct
    for i in range(0, len(lines)+1, 4):
        buttonAMatches = re.findall(BUTTON_A_REGEX, lines[i])
        buttonA = (int(buttonAMatches[0][0]), int(buttonAMatches[0][1]))
        buttonBMatches = re.findall(BUTTON_B_REGEX, lines[i+1])
        buttonB = (int(buttonBMatches[0][0]), int(buttonBMatches[0][1]))
        prizeMatches = re.findall(PRIZE_REGEX, lines[i+2])
        prize = (int(prizeMatches[0][0]) + 10000000000000, int(prizeMatches[0][1]) + 10000000000000)
        tokenCount += find_two_button_solution(buttonA, buttonB, prize)
    f.close()
    return tokenCount

if __name__ == "__main__":
    print(part1("day13Input.txt"))
    print(part2("day13Input.txt"))