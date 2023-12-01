import sys


def get_number(input: str):
    first_digit = 0
    for c in input:
        if c.isnumeric():
            first_digit = int(c)
            break

    last_digit = 0
    for c in reversed(input):
        if c.isnumeric():
            last_digit = int(c)
            break

    number = first_digit * 10 + last_digit
    return number


if __name__ == "__main__":
    input_files = sys.argv[1:]

    for input in input_files:
        with open(input) as f:
            input_data = f.readlines()

        answer = 0
        for i in input_data:
            answer += get_number(i)

        print("answer: ", answer)
