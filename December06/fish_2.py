fish = [int(f) for f in open("puzzle_input").read().strip().split(",")]
fish = [fish.count(i) for i in range(9)]

for _ in range(256):
    new = fish.pop(0)
    fish[-2] += new
    fish.append(new)

print(sum(fish))
