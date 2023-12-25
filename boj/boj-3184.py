from collections import deque


def bfs(start):
    global total_sheep
    global total_wolf
    sheep = 0
    wolf = 0
    Q = deque([start])
    visited[start[0]][start[1]] = 1

    while Q:
        r, c = Q.popleft()

        if board[r][c] == "o":
            sheep += 1

        if board[r][c] == "v":
            wolf += 1

        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]

            if nr < 0 or nr >= R or nc < 0 or nc >= C:
                continue

            if board[nr][nc] == "#" or visited[nr][nc] == 1:
                continue


            visited[nr][nc] = 1
            Q.append((nr, nc))

    if sheep > wolf:
        total_sheep += sheep
    else:
        total_wolf += wolf


R, C = map(int, input().split())

board = [list(input()) for _ in range(R)]
visited = [[0] * C for _ in range(R)]

dr = [1, 0, -1, 0]
dc = [0, -1, 0, 1]

total_sheep = 0
total_wolf = 0

for i in range(R):
    for j in range(C):
        if board[i][j] == "#" or visited[i][j] == 1:
            continue

        bfs((i, j))

print(total_sheep, total_wolf)
