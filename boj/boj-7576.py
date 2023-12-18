from collections import deque

dr = [0, 1, 0, -1]
dc = [-1, 0, 1, 0]


def bfs():
    Q = deque()

    for start in starts:
        Q.appendleft(start)
        dist[start[0]][start[1]] = 1

    while Q:
        curr = Q.pop()

        for i in range(4):
            nr = curr[0] + dr[i]
            nc = curr[1] + dc[i]

            if nr < 0 or nr >= N or nc < 0 or nc >= M:
                continue

            if (
                dist[curr[0]][curr[1]] + 1 >= dist[nr][nc] and dist[nr][nc] != 0
            ) or tomatoes[nr][nc] != 0:
                continue

            dist[nr][nc] = dist[curr[0]][curr[1]] + 1
            Q.appendleft((nr, nc))


M, N = map(int, input().split())

tomatoes = []
dist = [[0] * M for _ in range(N)]
for i in range(N):
    tomatoes.append(list(map(int, input().split())))

starts = []
for i in range(N):
    for j in range(M):
        if tomatoes[i][j] == 1:
            starts.append((i, j))

bfs()

fail = False
answer = -1

for i in range(N):
    if fail:
        break

    for j in range(M):
        if dist[i][j] > answer:
            answer = dist[i][j]
        if dist[i][j] == 0 and tomatoes[i][j] == 0:
            fail = True
            break

print((answer - 1) if not fail else -1)
