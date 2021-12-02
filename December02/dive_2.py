course = [
    tuple(instruction.split()) for instruction in open("puzzle_input").readlines()
]

x, y, aim = 0, 0, 0

for instruction, n in course:
    if instruction == "down":
        aim += int(n)
    elif instruction == "up":
        aim -= int(n)
    else:
        x += int(n)
        y += aim * int(n)

print(x * y)
