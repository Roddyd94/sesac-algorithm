from collections import deque
import sys

sys.stdin = open(f"input-{4875}.txt", "r")

dr = [1, 0, -1, 0]
dc = [0, 1, 0, -1]


def bfs(board, start, N):
    Q = deque()
    Q.appendleft(start)

    while Q:
        curr_pos = Q.pop()
        board[curr_pos[0]][curr_pos[1]] = -1

        for i in range(4):
            nr = curr_pos[0] + dr[i]
            nc = curr_pos[1] + dc[i]

            if nr >= N or nr < 0 or nc >= N or nc < 0:
                continue

            if board[nr][nc] == 3:
                return True

            if board[nr][nc] != 0:
                continue

            Q.appendleft((nr, nc))

    return False


T = int(input())

for test_case in range(1, T + 1):
    N = int(input())
    board = [list(map(int, input())) for _ in range(N)]

    start = (-1, -1)
    end = (-1, -1)

    for i in range(N):
        for j in range(N):
            if board[i][j] == 2:
                start = (i, j)

    answer = bfs(board, start, N)

    print(f"#{test_case} {1 if answer else 0}")
