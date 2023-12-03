import sys
from collections import namedtuple


class PartNumber(namedtuple("PartNumber", "number is_part")):
    def __repr__(self) -> str:
        return f"{self.number}({self.is_part})"


class Coordinate(namedtuple("Coordinate", "x y")):
    def __repr__(self) -> str:
        return f"[{self.x},{self.y}]"


def check_is_part(X: int, Y: int, num: int):
    _num = num
    number_len = 0
    while _num != 0:
        number_len += 1
        _num //= 10

    # print(f"  => {num}({number_len}): [{X}, {Y}]")

    coordinates_to_check: list[Coordinate] = []

    if Y > 0:
        if X > 0:
            coordinates_to_check.append(Coordinate(X - 1, Y - 1))
        for x in range(X, X + number_len):
            coordinates_to_check.append(Coordinate(x, Y - 1))
        if X + number_len < len(FList[0]):  # (-1) was common
            coordinates_to_check.append(Coordinate(X + number_len, Y - 1))

    if X + number_len < len(FList[0]):  # (-1) was common
        coordinates_to_check.append(Coordinate(X + number_len, Y))

    if Y < len(FList) - 1:
        if X + number_len < len(FList[0]):  # (-1) was common
            coordinates_to_check.append(Coordinate(X + number_len, Y + 1))
        for x in range(X + number_len - 1, X - 1, -1):
            coordinates_to_check.append(Coordinate(x, Y + 1))
        if X > 0:
            coordinates_to_check.append(Coordinate(X - 1, Y + 1))

    if X > 0:
        coordinates_to_check.append(Coordinate(X - 1, Y))

    # print(f"  => {num}: {coordinates_to_check}")

    nearby = []
    for coordinate in coordinates_to_check:
        char = ""

        try:
            char = FList[coordinate.y][coordinate.x]
            nearby.append(char)
            if (char != ".") and (not char.isnumeric()):
                return True
        except IndexError as e:
            print("=" * 5, e.args, "=" * 5)
            nearby.append("@")

    # print(f"  => {num} => {''.join(nearby)}")

    return False


def fun(F: str):
    ans_01 = 0

    global FList
    FList = F.split("\n")

    numbers: list[list[PartNumber]] = []
    for i, line in enumerate(FList):
        nums: list[PartNumber] = []
        symbols = ["."] * len(line)
        j = len(line)
        while j >= 0:
            j -= 1
            num = 0
            place = 1
            while j >= 0 and line[j].isnumeric():
                # symbols[j] = "0"
                num += int(line[j]) * place
                place *= 10
                j -= 1
            else:
                symbols[j] = line[j]

            if num:
                is_part = check_is_part(j + 1, i, num)
                nums.insert(0, PartNumber(num, is_part))
        numbers.append(nums)
        for n in nums:
            if n.is_part:
                ans_01 += n.number

    print("PART_01: ", ans_01)


if __name__ == "__main__":
    for file in sys.argv[1:]:
        print("#" * 10, file, "#" * 10)
        F = open(file).read().strip()
        # print(F)
        fun(F)
