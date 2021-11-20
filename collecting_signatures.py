# python3

from collections import namedtuple
from sys import stdin

Segment = namedtuple('Segment', 'start end')


def compute_optimal_points(segments):
    segments.sort(key=lambda x: x[1])

    coord = []
    n = len(segments)
    i = 0
    while i < n:
        curr = segments[i]
        while i < n - 1 and curr[1] >= segments[i + 1][0]:
            i += 1
        coord.append(curr[1])
        i += 1

    return coord


if __name__ == '__main__':
    n, *data = map(int, stdin.read().split())
    input_segments = list(map(lambda x: Segment(x[0], x[1]), zip(data[::2], data[1::2])))
    assert n == len(input_segments)
    output_points = compute_optimal_points(input_segments)
    print(len(output_points))
    print(*output_points)
