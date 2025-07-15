import sys


def part_one(one: list[tuple[int, int]], two: list[list[int]]):
    ans = 0

    for update in two:
        for u in reversed(range(len(update))):
            print(update[u], end=", ")
        print()

    return ans


def main():
    input_file = sys.argv[1]

    input_data: list[list[str]] = [[], []]
    section = 0
    with open(input_file) as f:
        lines = f.readlines()
        for line in lines:
            if line == "\n":
                section += 1
                continue
            input_data[section].append(line.strip())
    # print(input_data)

    input_one: list[tuple[int, int]] = []
    for i in input_data[0]:
        ii = list(map(int, i.split("|")))
        input_one.append((ii[0], ii[1]))
    # print(input_one)

    input_two: list[list[int]] = []
    for i in input_data[1]:
        ii = list(map(int, i.split(",")))
        input_two.append(ii)
    # print(input_two)

    ans_one = part_one(input_one, input_two)
    print("\nans_one:", ans_one)


if __name__ == "__main__":
    main()
