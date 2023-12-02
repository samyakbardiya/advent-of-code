import sys

VALID = {"red": 12, "green": 13, "blue": 14}


def part_01(F: str):
    answer = 0

    for line in F.split("\n"):
        line = line.strip()

        id = int(line.split(":")[0].split(" ")[1])
        game = line.split(":")[1].strip()

        is_valid = False
        for cube_set in game.split(";"):
            cube_set = cube_set.strip()
            cubes: dict[str, int] = {}

            for color_count in cube_set.split(","):
                color_count = color_count.strip()
                count, color = int(color_count.split(" ")[0]), color_count.split(" ")[1]
                cubes[color] = count

            is_valid = all(number <= VALID[color] for color, number in cubes.items())

            if not is_valid:
                break

        if is_valid:
            answer += id

    return answer


def part_02(F: str):
    answer = 0
    for line in F.split("\n"):
        line = line.strip()

        game = line.split(":")[1].strip()

        power = 1
        cubes: dict[str, int] = {}
        for cube_set in game.split(";"):
            cube_set = cube_set.strip()

            for color_count in cube_set.split(","):
                color_count = color_count.strip()

                count, color = int(color_count.split(" ")[0]), color_count.split(" ")[1]
                cubes[color] = max(count, cubes.get(color, 0))

        for color, count in cubes.items():
            power *= count

        answer += power

    return answer


if __name__ == "__main__":
    for file in sys.argv[1:]:
        F = open(file).read().strip()
        print(f"\n ===== {file} ===== ")
        print("PART 01", part_01(F))
        print("PART 02", part_02(F))
