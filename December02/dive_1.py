course = [
    tuple(instruction.split()) for instruction in open("puzzle_input").readlines()
]

x, y = 0, 0

for instruction, n in course:
    if instruction == "down":
        y += int(n)
    elif instruction == "up":
        y -= int(n)
    else:
        x += int(n)

print(x * y)
