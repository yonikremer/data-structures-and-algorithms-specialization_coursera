# python3

from sys import stdin


def maximum_loot_value(capacity, weights, prices):
    assert 0 <= capacity <= 2 * 10 ** 6
    assert len(weights) == len(prices)
    assert 1 <= len(weights) <= 10 ** 3
    assert all(0 < w <= 2 * 10 ** 6 for w in weights)
    assert all(0 <= p <= 2 * 10 ** 6 for p in prices)

    val_sum = 0

    rel_vals = []
    num_items = len(weights)
    
    for item in range(num_items):
        rel_vals.append(prices[item] / weights[item])
    
    while capacity > 0 and len(rel_vals) > 0:
        best_rel_val = max(rel_vals)
        i = rel_vals.index(best_rel_val)
        amount = min(capacity, weights[i])

        val_sum += amount * best_rel_val
        capacity -= amount

        weights.pop(i)
        prices.pop(i)
        rel_vals.pop(i)

    return val_sum


if __name__ == "__main__":
    data = list(map(int, stdin.read().split()))
    n, input_capacity = data[0:2]
    input_prices = data[2:(2 * n + 2):2]
    input_weights = data[3:(2 * n + 2):2]
    opt_value = maximum_loot_value(input_capacity, input_weights, input_prices)
    print("{:.10f}".format(opt_value))
