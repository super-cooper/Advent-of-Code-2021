import itertools

print(
    sum(
        sum(d2) > sum(d1)
        for d1, d2 in itertools.pairwise(
            [
                (a, b, c)
                for (a, _), (b, c) in itertools.pairwise(
                    itertools.pairwise(map(int, open("puzzle_input").readlines()))
                )
            ]
        )
    )
)
