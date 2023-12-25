from collections import deque
import sys

sys.stdin = open(f"input-{1953}.txt", "r")

types = [
    [0, 0, 0, 0],
    [1, 1, 1, 1],
    [1, 0, 1, 0],
    [0, 1, 0, 1],
    [1, 1, 0, 0],
    [0, 1, 1, 0],
    [0, 0, 1, 1],
    [1, 0, 0, 1],
]

dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]


def bfs(start):
    global L
    Q = deque([start])
    dist[start[0]][start[1]] = 1

    while Q:
        r, c = Q.popleft()
        if dist[r][c] >= L:
            break

        for i in range(4):
            if types[board[r][c]][i] == 0:
                continue

            nr = r + dr[i]
            nc = c + dc[i]

            if nr < 0 or nr >= N or nc < 0 or nc >= M:
                continue

            if dist[nr][nc] != 0 or types[board[nr][nc]][(i + 2) % 4] == 0:
                continue

            dist[nr][nc] = dist[r][c] + 1
            Q.append((nr, nc))


T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    answer = 0
    N, M, R, C, L = map(int, input().split())

    board = [list(map(int, input().split())) for _ in range(N)]
    dist = [[0] * M for _ in range(N)]
    start = (R, C)

    bfs(start)

    for i in range(N):
        for j in range(M):
            if dist[i][j] != 0:
                answer += 1

    print(f'#{test_case} {answer}')