from collections import defaultdict
import sys


def advent_of_code(file: str):
    ans_01 = 0
    ans_02 = 0

    points_earned = defaultdict(int)
    cards_earned = defaultdict(int)
    card_instance = defaultdict(lambda: 1)
    # card_instance[1] = 1
    # card_instance = defaultdict(int)

    for l, line in enumerate(file.split("\n")):  # noqa: E741
        data = line.split(":")[1]
        winning_data, my_data = data.split("|")
        winning_numbers = winning_data.split()
        my_numbers = my_data.split()
        # print(_, ",".join(winning_numbers), ",".join(my_numbers))

        count = defaultdict(int)

        for num in my_numbers:
            count[num] += 1
        for num in winning_numbers:
            count[num] -= 1

        wins = -1
        for k, v in count.items():
            if v == 0:
                wins += 1
        points = 2**wins
        points = points if points >= 1 else 0

        points_earned[l + 1] = points

        cards_earned[l + 1] = wins + 1

        card_instance[l + 1]  # init
        # print(l + 1, end=": ")
        for i in range(l + 2, l + cards_earned[l + 1] + 2):
            # print(i, end=" ")
            for _ in range(card_instance[l + 1]):
                # print("*", end="")
                card_instance[i] += 1
            # print(" | ", end="")
        # print()

        ans_01 += points

    for v in card_instance.values():
        ans_02 += v

    # print("points_won:", points_earned)
    # print("cards_instance:", cards_earned)
    # print("card_instance:", card_instance)

    print(" " * 3, "=" * 5, "PART_01:", ans_01, "=" * 5, "")
    print(" " * 3, "=" * 5, "PART_02:", ans_02, "=" * 5, "\n")


if __name__ == "__main__":
    for file in sys.argv[1:]:
        print("\n", "#" * 10, file, "#" * 10)
        F = open(file).read().strip()
        # print(F)
        advent_of_code(F)
