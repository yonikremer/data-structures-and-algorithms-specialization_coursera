# python3


def last_digit_of_the_sum_of_fibonacci_numbers_again_naive(from_index, to_index):
    assert 0 <= from_index <= to_index <= 10 ** 18

    if to_index == 0:
        return 0

    fibonacci_numbers = [0] * (to_index + 1)
    fibonacci_numbers[0] = 0
    fibonacci_numbers[1] = 1
    for i in range(2, to_index + 1):
        fibonacci_numbers[i] = fibonacci_numbers[i - 2] + fibonacci_numbers[i - 1]

    return sum(fibonacci_numbers[from_index:to_index + 1]) % 10


def last_digit_of_the_sum_of_fibonacci_numbers(n):

    prev, curr = 0, 1

    if 2 > n >= 0:
        return n

    s = 1
    n_remainder = n % 60
    if 2 > n_remainder >= 0:
        return n_remainder
    for _ in range(n_remainder - 1):
        prev, curr = curr, (prev + curr) % 10
        s += (curr % 10)
        s = s % 10

    return s


def last_digit_of_the_sum_of_fibonacci_numbers_again(from_index, to_index):
    assert 0 <= from_index <= to_index <= 10 ** 18

    return (last_digit_of_the_sum_of_fibonacci_numbers(to_index) - last_digit_of_the_sum_of_fibonacci_numbers(from_index-1)) % 10


if __name__ == '__main__':
    input_from, input_to = map(int, input().split())
    print(last_digit_of_the_sum_of_fibonacci_numbers_again(input_from, input_to))
