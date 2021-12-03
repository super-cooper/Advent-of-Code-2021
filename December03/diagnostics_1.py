import collections
from functools import reduce

bits = [line.strip() for line in open("puzzle_input").readlines()]
print(
    reduce(
        (lambda g, e: g * e),
        [
            int("".join(x), 2)
            for x in zip(
                *map(
                    lambda c: (c[0][0], c[1][0]),
                    [
                        collections.Counter(line[pos] for line in bits).most_common()
                        for pos in range(len(bits[0]))
                    ],
                )
            )
        ],
    )
)
