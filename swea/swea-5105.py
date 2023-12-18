from collections import deque
import sys

sys.stdin = open(f"input-{5105}.txt", "r")

dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]


def bfs(board, dist, r, c):
    Q = deque()

    Q.append((r, c))

    while Q:
        r, c = Q.popleft()

        for i in range(4):
            nr, nc = r + dr[i], c + dc[i]

            if nr < 0 or nr >= N or nc < 0 or nc >= N:
                continue

            if board[nr][nc] == 1 or dist[nr][nc] != 0:
                continue

            if board[nr][nc] == 3:
                return dist[r][c] + 1

            dist[nr][nc] = dist[r][c] + 1
            Q.append((nr, nc))

    return 0


T = int(input())

for test_case in range(1, T + 1):
    N = int(input())

    board = [list(map(int, input())) for _ in range(N)]
    dist = [[0] * N for _ in range(N)]

    start = (-1, -1)

    r, c = -1, -1
    for i in range(N):
        for j in range(N):
            if board[i][j] == 2:
                r, c = i, j
                dist[i][j] = 1

    answer = bfs(board, dist, r, c) - 2
    answer = max(answer, 0)

    print(f"#{test_case} {answer}")
