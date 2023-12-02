import sys
from collections import defaultdict

VALID = {"red": 12, "green": 13, "blue": 14}


def fun(F: str):
    ans_01 = 0
    ans_02 = 0

    for L in F.split("\n"):
        id_, game = L.split(":")
        _, id_ = id_.split()

        ok = True
        MIN = defaultdict(int)
        cubes: dict[str, int] = {}
        for sets in game.split(";"):
            for cube in sets.split(","):
                n, color = cube.split()
                cubes[color] = int(n)

                MIN[color] = max(int(n), MIN[color])

                if cubes[color] > VALID[color]:
                    ok = False

        if ok:
            ans_01 += int(id_)

        power = 1
        for m in MIN.values():
            power *= m
        ans_02 += power

    print(f"ANS_01: {ans_01}")
    print(f"ANS_02: {ans_02}")


if __name__ == "__main__":
    for file in sys.argv[1:]:
        print(f"\n ===== {file} ===== ")
        fun(open(file).read().strip())
