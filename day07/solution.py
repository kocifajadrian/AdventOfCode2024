# problem: https://adventofcode.com/2024/day/7


import operator


def read_file() -> None:
    with open(file_name, "r") as file:
        for line in file:
            value, numbers = line.strip().split(":")
            equations.append((int(value), [int(x) for x in numbers.strip().split(" ")]))


def concatenation(a: int, b: int) -> int:
    return int(str(a) + str(b))


def solve(operators: list[operator]) -> int:
    result = 0
    for value, numbers in equations:
        storage = list()
        storage.append(numbers[0])
        for number in numbers[1:]:
            helper = list()
            for previous in storage:
                for o in operators:
                    helper.append(o(previous, number))
            storage = helper.copy()
        if value in storage:
            result += value
    return result


def first_star() -> int:
    return solve([operator.add, operator.mul])


def second_star() -> int:
    return solve([operator.add, operator.mul, concatenation])


if __name__ == "__main__":
    file_name = "input.txt"
    equations = list()
    read_file()
    print(first_star())     # 42283209483350
    print(second_star())    # 1026766857276279
