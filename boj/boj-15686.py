def distance(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])


def calc_distances():
    distances = 0
    for house in houses:
        nearest_chicken = distance(house, sel[0])
        for i in range(1, M):
            nearest_chicken = min(nearest_chicken, distance(house, sel[i]))

        distances += nearest_chicken

    return distances


def comb(ix, six):
    global answer
    if six == M:
        answer = min(answer, calc_distances())
        return

    if ix == K:
        return

    sel[six] = chickens[ix]

    comb(ix + 1, six + 1)
    comb(ix + 1, six)


N, M = map(int, input().split())

board = [list(map(int, input().split())) for _ in range(N)]

answer = 10000
sel = [0] * M
chickens = []
houses = []

for i in range(N):
    for j in range(N):
        if board[i][j] == 1:
            houses.append((i, j))
        if board[i][j] == 2:
            chickens.append((i, j))

K = len(chickens)

comb(0, 0)

print(answer)
