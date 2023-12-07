from functools import reduce
import sys
from collections import namedtuple


class Coordinate(namedtuple("Coordinate", "x y")):
    def __repr__(self) -> str:
        return f"[{self.x},{self.y}]"


def search_nearby(i: int, j: int):
    symbol = FList[i][j]

    nearby_coordinates: list[Coordinate] = []
    for x in range(max(0, i - 1), min(len(FList), i + 2)):
        for y in range(max(0, j - 1), min(len(FList[0]), j + 2)):
            if x == i and y == j:
                continue
            nearby_coordinates.append(Coordinate(x, y))

    # print(f"[{i},{j}] {symbol}: {nearby_coordinates}")

    numbers: list[int] = []
    for coord in nearby_coordinates:
        digits: list[int]
        char = FList[coord.x][coord.y]
        if char.isnumeric():
            digits = [int(char)]

            # go left
            left = coord.y - 1
            while left >= 0 and FList[coord.x][left].isnumeric():
                curr_coord = Coordinate(coord.x, left)
                if curr_coord in nearby_coordinates:
                    nearby_coordinates.remove(curr_coord)
                digits.insert(0, int(FList[curr_coord.x][curr_coord.y]))
                left -= 1

            # go left
            right = coord.y + 1
            while right <= len(FList[0]) - 1 and FList[coord.x][right].isnumeric():
                curr_coord = Coordinate(coord.x, right)
                if curr_coord in nearby_coordinates:
                    nearby_coordinates.remove(curr_coord)
                digits.append(int(FList[curr_coord.x][curr_coord.y]))
                right += 1

            number = reduce(lambda x, y: x * 10 + y, digits)
            numbers.append(number)

            global ANS_01
            ANS_01 += number

    global ANS_02
    if symbol == "*" and len(numbers) == 2:
        ANS_02 += reduce(lambda x, y: x * y, numbers)

    # print(f"[{i},{j}] {symbol}: {numbers}")


def advent_of_code(F: str):
    global FList, ANS_01, ANS_02
    FList = F.split("\n")
    ANS_01 = 0
    ANS_02 = 0

    for i, line in enumerate(FList):
        for j, char in enumerate(line):
            if not (char.isnumeric() or char == "."):
                search_nearby(i, j)

    print(" " * 3, "=" * 5, "PART_01:", ANS_01, "=" * 5, "")
    print(" " * 3, "=" * 5, "PART_02:", ANS_02, "=" * 5, "\n")


if __name__ == "__main__":
    for file in sys.argv[1:]:
        print("#" * 10, file, "#" * 10)
        F = open(file).read().strip()
        # print(F)
        advent_of_code(F)
