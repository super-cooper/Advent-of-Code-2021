import collections
from functools import reduce

print(
    reduce(
        (lambda o, c: o * c),
        map(
            lambda m: (
                lambda g, h, i=0: (lambda f, j, k, l: f(f, j, k, l))(
                    lambda y, bits, most, pos: y(
                        y,
                        list(
                            filter(
                                (
                                    lambda b: b[pos]
                                    == (
                                        criteria := collections.Counter(
                                            line[pos] for line in bits
                                        ).most_common()
                                    )[
                                        1 - most
                                        if criteria[0][1] != criteria[1][1]
                                        else [x[0] for x in criteria].index(str(most))
                                    ][
                                        0
                                    ]
                                ),
                                bits,
                            )
                        ),
                        most,
                        pos + 1,
                    )
                    if len(bits) > 1
                    else int("".join(bits[0]), 2),
                    g,
                    h,
                    i,
                )
            )([line.strip() for line in open("puzzle_input").readlines()], m),
            (1, 0),
        ),
    )
)
