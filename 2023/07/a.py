import sys
from collections import defaultdict


def find_ponits(cards: str):
    print("cards:", cards)
    card = defaultdict(int)
    for c in cards:
        card[c] += 1

    card_count: list[int] = []
    for _, v in card.items():
        card_count.append(v)

    card_count.sort(reverse=True)
    print("sorted_card_count:", card_count)

    print("card:", card)
    return card


def advent_of_code(file: list[str]):
    ans_01 = 0
    ans_02 = 0

    cards_list: list[str] = []
    bids_list: list[int] = []

    for f in file:
        value = f.split()
        if not value:
            break
        cards_list.append(value[0])
        bids_list.append(int(value[1]))

        card_point = find_ponits(value[0])
        print("card_point:", card_point)

    print("cards_list:", cards_list)
    print("bids_list:", bids_list)

    print(" " * 3, "=" * 5, "PART_01:", ans_01, "=" * 5, "")
    print(" " * 3, "=" * 5, "PART_02:", ans_02, "=" * 5, "")


if __name__ == "__main__":
    for file in sys.argv[1:]:
        print("\n", "#" * 10, file, "#" * 10)
        F = open(file).read().split("\n")
        advent_of_code(F)
