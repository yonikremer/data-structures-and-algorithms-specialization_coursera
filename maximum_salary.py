# python3

from itertools import permutations


def largest_number_naive(numbers):
    numbers = list(map(str, numbers))

    largest = 0

    for permutation in permutations(numbers):
        largest = max(largest, int("".join(permutation)))

    return largest


def val(num):
    # temp = 0
    # skip = 12
    # if 10 ** 3 <= num < 10 ** 4:
    #     skip = 4
    # elif 10 ** 2 <= num < 10 ** 3:
    #     skip = 3
    # elif 10 ** 1 <= num < 10 ** 2:
    #     skip = 2
    # elif 10 ** 0 <= num < 10 ** 1:
    #     skip = 1
    # for i in range(0, 12, skip):
    #     temp += num * (10 ** i)
    # return temp
    s = str(num)
    length = len(s)
    return s * int(12 / length)


def largest_number(numbers):
    numbers = [int(x) for x in numbers]
    numbers.sort(reverse=True, key=val)
    s = ""
    for curr in numbers:
        s += str(curr)
    return int(s)


if __name__ == '__main__':
    n = int(input())
    input_numbers = input().split()
    assert len(input_numbers) == n
    print(largest_number(input_numbers))
