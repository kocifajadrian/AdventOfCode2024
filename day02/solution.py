# problem: https://adventofcode.com/2024/day/2


def read_file() -> None:
    with open(file_name, "r") as file:
        for line in file:
            reports.append([int(x) for x in line.split()])


def is_valid1(elements: list[int], increasing: bool) -> bool:
    for i in range(len(elements) - 1):
        value = elements[i] - elements[i + 1]
        if increasing:
            value = elements[i + 1] - elements[i]
        if value < 1 or value > 3:
            return False
    return True


def is_valid2(elements: list[int], increasing: bool) -> bool:
    for i in range(len(elements) - 1):
        value = elements[i] - elements[i + 1]
        if increasing:
            value = elements[i + 1] - elements[i]
        if value < 1 or value > 3:
            elements1 = elements.copy()
            elements2 = elements.copy()
            elements1.pop(i)
            elements2.pop(i + 1)
            return (is_valid1(elements1, increasing) or
                    is_valid1(elements2, increasing))
    return True


def first_star() -> int:
    result = 0
    for report in reports:
        if (is_valid1(report, True) or
                is_valid1(report, False)):
            result += 1
    return result


def second_star() -> int:
    result = 0
    for report in reports:
        if (is_valid2(report, True) or
                is_valid2(report, False)):
            result += 1
    return result


if __name__ == "__main__":
    file_name = "input.txt"
    reports = list()
    read_file()
    print(first_star())     # 379
    print(second_star())    # 430
