from collections import deque

T = int(input())

dr = [1, 0, -1, 0]
dc = [0, 1, 0, -1]


def bfs(start):
    Q = deque()
    Q.appendleft(start)

    while Q:
        curr = Q.pop()

        for i in range(4):
            nr = curr[0] + dr[i]
            nc = curr[1] + dc[i]

            if nr < 0 or nr >= N or nc < 0 or nc >= M:
                continue

            if farm[nr][nc] != 1:
                continue

            farm[nr][nc] = 2
            Q.appendleft((nr, nc))

    pass


for tc in range(T):
    M, N, K = map(int, input().split())

    farm = [[0] * M for _ in range(N)]

    for i in range(K):
        c, r = map(int, input().split())
        farm[r][c] = 1

    area = 0
    for i in range(N):
        for j in range(M):
            if farm[i][j] == 1:
                bfs((i, j))
                area += 1

    print(area)
