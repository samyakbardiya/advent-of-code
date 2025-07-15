import sys


def part_one(input: list[list[str]]):
    ans = 0

    len_x = len(input[0])
    len_y = len(input)

    xy_cord: list[tuple[int, int]] = []

    target = "XMAS"

    def find_north(x, start_y):
        end_y = start_y - len(target)
        if end_y < -1:
            return False
        _range = range(start_y, end_y, -1)
        xmas = "".join(input[y][x] for y in _range)
        cord = [(y, x) for y in _range]
        if xmas == target:
            xy_cord.extend(cord)
            return True

    def find_east(start_x, y):
        end_x = start_x + len(target)
        if end_x > len_x:
            return False
        _range = range(start_x, end_x)
        xmas = "".join(input[y][x] for x in _range)
        cord = [(y, x) for y in _range]
        if xmas == target:
            xy_cord.extend(cord)
            return True

    def find_west(start_x, y):
        end_x = start_x - len(target)
        if end_x < -1:
            return False
        _range = range(start_x, end_x, -1)
        xmas = "".join(input[y][x] for x in _range)
        cord = [(y, x) for y in _range]
        if xmas == target:
            xy_cord.extend(cord)
            return True

    def find_south(x, start_y):
        end_y = start_y + len(target)
        if end_y > len_y:
            return False
        _range = range(start_y, end_y)
        xmas = "".join(input[y][x] for y in _range)
        cord = [(y, x) for y in _range]
        if xmas == target:
            xy_cord.extend(cord)
            return True

    def find_north_east(start_x, start_y):
        end_x = start_x + len(target)
        end_y = start_y - len(target)
        if end_x > len_x or end_y < -1:
            return False
        _range_y = range(start_y, end_y, -1)
        _range_x = range(start_x, end_x)
        xmas = "".join(input[y][x] for y, x in zip(_range_y, _range_x))
        cord = [(y, x) for y, x in zip(_range_y, _range_x)]
        if xmas == target:
            xy_cord.extend(cord)
            return True

    def find_south_east(start_x, start_y):
        end_x = start_x + len(target)
        end_y = start_y + len(target)
        if end_x > len_x or end_y > len_y:
            return False
        _range_y = range(start_y, end_y)
        _range_x = range(start_x, end_x)
        xmas = "".join(input[y][x] for y, x in zip(_range_y, _range_x))
        cord = [(y, x) for y, x in zip(_range_y, _range_x)]
        if xmas == target:
            xy_cord.extend(cord)
            return True

    def find_south_west(start_x, start_y):
        end_x = start_x - len(target)
        end_y = start_y + len(target)
        if end_x < -1 or end_y > len_y:
            return False
        _range_y = range(start_y, end_y)
        _range_x = range(start_x, end_x, -1)
        xmas = "".join(input[y][x] for y, x in zip(_range_y, _range_x))
        cord = [(y, x) for y, x in zip(_range_y, _range_x)]
        if xmas == target:
            xy_cord.extend(cord)
            return True

    def find_north_west(start_x, start_y):
        end_x = start_x - len(target)
        end_y = start_y - len(target)
        if end_x < -1 or end_y < -1:
            return False
        _range_y = range(start_y, end_y, -1)
        _range_x = range(start_x, end_x, -1)
        xmas = "".join(input[y][x] for y, x in zip(_range_y, _range_x))
        cord = [(y, x) for y, x in zip(_range_y, _range_x)]
        if xmas == target:
            xy_cord.extend(cord)
            return True

    def find_them_all(x, y):
        ans = 0
        if find_north(x, y):
            ans += 1
        if find_east(x, y):
            ans += 1
        if find_west(x, y):
            ans += 1
        if find_south(x, y):
            ans += 1
        if find_north_east(x, y):
            ans += 1
        if find_south_east(x, y):
            ans += 1
        if find_south_west(x, y):
            ans += 1
        if find_north_west(x, y):
            ans += 1
        return ans

    for y in range(len_y):
        for x in range(len_x):
            if input[y][x] == "X":
                ans += find_them_all(x, y)

    xy_cord_set = set(xy_cord)
    # for y in range(len_y):
    #     row = [input[y][x] if (y, x) in xy_cord_set else "." for x in range(len_x)]
    #     print("".join(row))
    print(
        "\n".join(
            "".join(
                (str(input[y][x] if (y, x) in xy_cord_set else "."))
                for x in range(len_x)
            )
            for y in range(len_y)
        )
    )

    # freq_matrix = [[0 for _ in range(len_x)] for _ in range(len_y)]
    # for y in range(len_y):
    #     for x in range(len_x):
    #         if (y, x) in xy_cord:
    #             freq_matrix[y][x] += 1
    # print("\n".join("".join(str(cell) for cell in row) for row in freq_matrix))

    return ans


def part_two(input: list[list[str]]):
    ans = 0

    len_x = len(input[0])
    len_y = len(input)

    xy_cord: list[tuple[int, int]] = []

    def find_north_east(x, y):
        pass

    def find_south_west(x, y):
        pass

    def find_south_east(x, y):
        pass

    def find_north_west(x, y):
        pass

    def find_them_all(x, y):
        ans = 0
        backslash = find_north_east(x - 1, y - 1) or find_south_west(x + 1, y + 1)
        foreslash = find_north_west(x + 1, y + 1) or find_south_east(x - 1, y - 1)
        if (backslash) and (foreslash):
            ans += 1
        return ans

    for y in range(len_y):
        for x in range(len_x):
            if input[y][x] == "A":
                ans += find_them_all(x, y)


def main():
    input_file = sys.argv[1]

    input_data = []
    with open(input_file) as f:
        lines = f.readlines()
        for line in lines:
            input_data.append(list(line.strip()))

    # print("input_data:", json.dumps(input_data, indent=4))
    ans_one = part_one(input_data)
    print("\nans_one:", ans_one)


if __name__ == "__main__":
    main()
