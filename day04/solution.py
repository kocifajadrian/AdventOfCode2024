# problem: https://adventofcode.com/2024/day/4


def read_file() -> None:
    with open(file_name, "r") as file:
        for line in file:
            text.append(line.strip())


def in_bounds(y: int, x: int) -> bool:
    return 0 <= y < len(text) and 0 <= x < len(text[0])


def count_xmas_from_position(y: int, x: int) -> int:
    counter = 0
    word = "XMAS"
    for dy, dx in directions:
        condition = True
        for i in range(len(word)):
            yy = y + i * dy
            xx = x + i * dx
            if not in_bounds(yy, xx) or text[yy][xx] != word[i]:
                condition = False
                break
        if condition:
            counter += 1
    return counter


def is_double_mas_from_position(y: int, x: int) -> bool:
    if text[y][x] != "A":
        return False
    if not in_bounds(y - 1, x - 1) or not in_bounds(y + 1, x + 1):
        return False
    word1 = text[y - 1][x - 1] + text[y][x] + text[y + 1][x + 1]
    word2 = text[y + 1][x - 1] + text[y][x] + text[y - 1][x + 1]
    options = ["MAS", "SAM"]
    if word1 in options and word2 in options:
        return True
    return False


def first_star() -> int:
    result = 0
    for y in range(len(text)):
        for x in range(len(text[0])):
            result += count_xmas_from_position(y, x)
    return result


def second_star() -> int:
    result = 0
    for y in range(len(text)):
        for x in range(len(text[0])):
            if is_double_mas_from_position(y, x):
                result += 1
    return result


if __name__ == "__main__":
    file_name = "input.txt"
    text = []
    read_file()
    directions = [(0, -1), (0, 1), (-1, 0), (1, 0),
                  (-1, -1), (-1, 1), (1, -1), (1, 1)]
    print(first_star())     # 2560
    print(second_star())    # 1910
