# python3


def compute_optimal_summands(n):
    assert 1 <= n <= 10 ** 9
    summands = []

    total = 0
    i = 1
    while n >= total + 2 * i + 1:
        summands.append(i)
        total += i
        i += 1

    summands.append(n - total)

    return summands


if __name__ == '__main__':
    input_n = int(input())
    output_summands = compute_optimal_summands(input_n)
    print(len(output_summands))
    print(*output_summands)
