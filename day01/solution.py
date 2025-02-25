# problem: https://adventofcode.com/2024/day/1


def read_file() -> None:
    with open(file_name, "r") as file:
        for line in file:
            n1, n2 = [int(x) for x in line.split("   ")]
            numbers1.append(n1)
            numbers2.append(n2)


def first_star() -> int:
    result = 0
    nums1 = sorted(numbers1)
    nums2 = sorted(numbers2)
    for i in range(len(nums1)):
        result += abs(nums2[i] - nums1[i])
    return result


def second_star() -> int:
    result = 0
    for number in numbers1:
        result += number * numbers2.count(number)
    return result


if __name__ == "__main__":
    file_name = "input.txt"
    numbers1 = list()
    numbers2 = list()
    read_file()
    print(first_star())     # 3508942
    print(second_star())    # 26593248
