# problem: https://adventofcode.com/2024/day/6


def read_file() -> None:
    with open(file_name, "r") as file:
        for line in file:
            room.append(list(line.strip()))


def find_start() -> tuple[int, int]:
    for y in range(len(room)):
        for x in range(len(room[0])):
            if room[y][x] == "^":
                return y, x
    return -1, -1


def in_bounds(position: tuple[int, int]) -> bool:
    return 0 <= position[0] < len(room) and 0 <= position[1] < len(room[0])


def turn_right(direction: tuple[int, int]) -> tuple[int, int]:
    new = direction[1], direction[0]
    if direction[0]:
        new = -1 * new[0], -1 * new[1]
    return new


def move(position: tuple[int, int],
         direction: tuple[int, int]) -> [tuple[int, int], tuple[int, int]]:
    new_position = position[0] + direction[0], position[1] + direction[1]
    if not in_bounds(new_position):
        return [new_position, direction]
    if room[new_position[0]][new_position[1]] == "#":
        new_direction = turn_right(direction)
        return position, new_direction
    return new_position, direction


def first_star() -> int:
    visited = set()
    position = start_position
    direction = start_direction
    while in_bounds(position):
        visited.add(position)
        position, direction = move(position, direction)
    return len(visited)


if __name__ == "__main__":
    file_name = "input.txt"
    room = list()
    start = list()
    read_file()
    start_position = find_start()
    start_direction = (-1, 0)
    print(first_star())     # 5095
