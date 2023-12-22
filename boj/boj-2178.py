from collections import deque

dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]


def bfs(start):
    Q = deque([start])
    dist[start[0]][start[1]] = 1

    while Q:
        r, c = Q.pop()

        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]

            if nr >= N or nr < 0 or nc >= M or nc < 0:
                continue

            if board[nr][nc] == 0 or dist[nr][nc] != 0:
                continue

            if nr == N - 1 and nc == M - 1:
                return dist[r][c]

            dist[nr][nc] = dist[r][c] + 1
            Q.appendleft((nr, nc))


N, M = map(int, input().split())

board = [list(map(int, input())) for _ in range(N)]
dist = [[0] * M for _ in range(N)]

answer = bfs((0, 0)) + 1

print(answer)
