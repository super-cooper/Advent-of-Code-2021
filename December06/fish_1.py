fish = [int(f) for f in open("puzzle_input").read().strip().split(",")]

for _ in range(80):
    new = 0
    for i, f in enumerate(fish):
        if f == 0:
            new += 1
            fish[i] = 6
        else:
            fish[i] -= 1
    fish += [8] * new

print(len(fish))
