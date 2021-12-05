from collections import defaultdict

lines = [
    [[int(x) for x in p.split(",")] for p in line.strip().split(" -> ")]
    for line in open("puzzle_input").readlines()
]

intersections = defaultdict(int)

for ((x1, y1), (x2, y2)) in lines:
    for p in (
        [(x1, y) for y in range(min(y1, y2), max(y1, y2) + 1)]
        if x1 == x2
        else (
            [(x, y1) for x in range(min(x1, x2), max(x1, x2) + 1)] if y1 == y2 else []
        )
    ):
        intersections[p] += 1

print(sum(int(intersections[p] > 1) for p in intersections))
