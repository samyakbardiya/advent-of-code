import sys


def compute_wining_ways(time: list[int], distance: list[int]):
    ans = 1

    for i in range(len(time)):
        left_nth = 0
        left_distance = 0
        for t in range(time[i]):
            left_distance = t * (time[i] - t)
            left_nth = t
            if left_distance > distance[i]:
                break

        right_nth = len(time)
        right_distance = 0
        for t in range(time[i] + 1, 0, -1):
            right_distance = t * (time[i] - t)
            right_nth = t
            if right_distance > distance[i]:
                break

        ans *= right_nth - left_nth + 1

    return ans


def advent_of_code(file: list[str]):
    time_01: list[int] = [int(i) for i in file[0].split()[1:]]
    distance_01: list[int] = [int(i) for i in file[1].split()[1:]]
    ans_01 = compute_wining_ways(time_01, distance_01)

    time_02 = [int("".join(file[0].split()[1:]))]
    distance_02 = [int("".join(file[1].split()[1:]))]
    ans_02 = compute_wining_ways(time_02, distance_02)

    print(" " * 3, "=" * 5, "PART_01:", ans_01, "=" * 5, "")
    print(" " * 3, "=" * 5, "PART_02:", ans_02, "=" * 5, "")


if __name__ == "__main__":
    for file in sys.argv[1:]:
        print("\n", "#" * 10, file, "#" * 10)
        F = open(file).read().split("\n")
        advent_of_code(F)
