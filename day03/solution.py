# problem: https://adventofcode.com/2024/day/3


import re


def read_file() -> None:
    with open(file_name, "r") as file:
        for line in file:
            instructions.append(line.strip())


def mul_number(string) -> int:
    left, right = string.split(",")
    number1 = int(left[4:])
    number2 = int(right[:-1])
    return number1 * number2


def first_star() -> int:
    result = 0
    pattern = r"mul\(\d{1,3},\d{1,3}\)"
    for line in instructions:
        matches = re.findall(pattern, line)
        result += sum(mul_number(match) for match in matches)
    return result


def second_star() -> int:
    result = 0
    patterns = r"mul\(\d{1,3},\d{1,3}\)|do\(\)|don't\(\)"
    enabled = True
    for line in instructions:
        matches = re.findall(patterns, line)
        for match in matches:
            if match == "do()":
                enabled = True
            elif match == "don't()":
                enabled = False
            elif enabled:
                result += mul_number(match)
    return result


if __name__ == "__main__":
    file_name = "input.txt"
    instructions = list()
    read_file()
    print(first_star())     # 181345830
    print(second_star())    # 98729041
