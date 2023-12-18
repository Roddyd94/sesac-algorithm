from functools import reduce


def count_mine(board_mine, r, c):
    if board_mine[r][c] == "*":
        return "*"

    dr = [0, 1, 1, 1, 0, -1, -1, -1]
    dc = [1, 1, 0, -1, -1, -1, 0, 1]

    max_length = len(board_mine)

    result = 0

    for i in range(len(dc)):
        if (
            r + dr[i] >= 0
            and r + dr[i] < max_length
            and c + dc[i] >= 0
            and c + dc[i] < max_length
        ):
            result += 1 if board_mine[r + dr[i]][c + dc[i]] == "*" else 0

    return result


N = int(input())

found = False
board_mine = []
board_found = []
for i in range(N):
    board_mine.append(list(input()))

for i in range(N):
    board_found.append(list(input()))

for i in range(N):
    for j in range(N):
        if board_found[i][j] != "x":
            continue

        board_found[i][j] = count_mine(board_mine, i, j)
        if board_found[i][j] == "*":
            found = True

if found:
    for i in range(N):
        for j in range(N):
            if board_mine[i][j] == "*":
                board_found[i][j] = "*"


for i in range(N):
    print(reduce(lambda x, y: f"{x}{y}", board_found[i]))
