# CORRECT FOR 2ND
import sys

NUMBER_NAMES = [
    "zero",
    "one",
    "two",
    "three",
    "four",
    "five",
    "six",
    "seven",
    "eight",
    "nine",
]


def get_number(input: str):
    first_digit = -1
    for i in range(len(input)):
        if first_digit != -1:
            break

        if input[i].isnumeric():
            first_digit = int(input[i])

        for j in range(len(NUMBER_NAMES)):
            if NUMBER_NAMES[j] in input[:i]:
                first_digit = j

    last_digit = -1
    for i in reversed(range(len(input))):
        if last_digit != -1:
            break

        if input[i].isnumeric():
            last_digit = int(input[i])

        for j in range(len(NUMBER_NAMES)):
            if NUMBER_NAMES[j] in input[i:]:
                last_digit = j

    print(f"{first_digit}, {last_digit} <== {input}")
    number = first_digit * 10 + last_digit
    return number


if __name__ == "__main__":
    input_files = sys.argv[1:]

    for input in input_files:
        print(f"\n===== {input} =====")
        with open(input) as f:
            input_data = f.readlines()

        answer = 0
        for i in input_data:
            answer += get_number(i)

        print("answer: ", answer)
