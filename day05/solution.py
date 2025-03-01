# problem: https://adventofcode.com/2024/day/5


def read_file() -> None:
    with open(file_name, "r") as file:
        first_part = True
        for line in file:
            line = line.strip()
            if line == "":
                first_part = False
                continue
            if first_part:
                rules.append([int(x) for x in line.split("|")])
            else:
                updates.append([int(x) for x in line.split(",")])


def is_correct_order(e1: int, e2: int, update: list[int]) -> bool:
    try:
        if update.index(e1) <= update.index(e2):
            return True
    except ValueError:
        return True
    return False


def exchange_positions(e1: int, e2: int, update: list[int]) -> None:
    i1 = update.index(e1)
    i2 = update.index(e2)
    update[i1], update[i2] = e2, e1


def first_star() -> int:
    result = 0
    for update in updates:
        is_correct = True
        for rule in rules:
            if not is_correct_order(rule[0], rule[1], update):
                is_correct = False
                break
        if is_correct:
            result += update[(len(update) - 1) // 2]
    return result


def second_star() -> int:
    result = 0
    for update in updates:
        change = False
        while True:
            all_correct = True
            for rule in rules:
                if not is_correct_order(rule[0], rule[1], update):
                    exchange_positions(rule[0], rule[1], update)
                    change = True
                    all_correct = False
            if all_correct:
                break
        if change:
            result += update[(len(update) - 1) // 2]
    return result


if __name__ == "__main__":
    file_name = "input.txt"
    rules = list()
    updates = list()
    read_file()
    print(first_star())     # 6498
    print(second_star())    # 5017
