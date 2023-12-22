from functools import reduce

board = [list(map(int, input().split())) for _ in range(5)]

dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]

routes = set()


def dfs(curr, route: list):
    r, c = curr
    route.append(board[r][c])

    if len(route) == 6:
        routes.add(reduce(lambda x, y: f"{x}{y}", route))
        return

    for i in range(4):
        nr = r + dr[i]
        nc = c + dc[i]

        if nr >= 5 or nr < 0 or nc >= 5 or nc < 0:
            continue

        dfs((nr, nc), route[:])


for i in range(5):
    for j in range(5):
        dfs((i, j), [])

print(len(routes))
