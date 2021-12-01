import itertools

print(
    sum(
        d2 > d1
        for d1, d2 in itertools.pairwise(map(int, open("puzzle_input").readlines()))
    )
)
