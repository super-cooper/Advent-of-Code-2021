puz = [line.strip() for line in open("puzzle_input").readlines() if line.strip() != ""]
drawing = [int(x) for x in puz.pop(0).split(",")]
boards = [[int(x) for x in line.split()] for line in puz]
winners = []

for n in drawing:
    remove = []
    boards = [[None if x == n else x for x in row] for row in boards]
    for i in range(0, len(boards), 5):
        if any(all(k is None for k in boards[i + j]) for j in range(5)) or any(
            all(boards[i + j][k] is None for j in range(5)) for k in range(5)
        ):
            winners.append(
                sum(
                    sum(x if (x := board[j]) is not None else 0 for j in range(5))
                    for board in boards[i : i + 5]
                )
                * n
            )
            for a in range(i, i + 5):
                for b in range(5):
                    boards[a][b] = -1

print(winners[-1])
