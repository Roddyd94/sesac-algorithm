dr = [-1, 0, 1, 0]
dc = [0, -1, 0, 1]


def BFS(r, c):
    Q = []
    Q.append((r, c))

    dist[r][c] = 1

    while Q:
        curr_r, curr_c = Q.pop(0)

        for i in range(4):
            nr = curr_r + dr[i]
            nc = curr_c + dc[i]

            if nr < 0 or nr >= N or nc < 0 or nc >= N:
                continue

            if arr[nr][nc] == 0 or dist[nr][nc] != 0:
                continue

            Q.append((nr, nc))
            dist[nr][nc] = dist[curr_r][curr_c] + 1


N = int(input())
arr = [list(map(int, input())) for _ in range(N)]
dist = [[0] * N for _ in range(N)]

for i in range(N):
    for j in range(N):
        if arr[i][j] == 1 and dist[i][j] == 0:
            BFS(i, j)

for d in dist:
    print(*d)
