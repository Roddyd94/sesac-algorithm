def perm(depth, acc):
    global answer

    if depth == N:
        acc += G[sel[depth - 1]][sel[0]]
        # print(*sel, ":", acc)
        answer = min(answer, acc)
        return

    if acc > answer:
        return

    for i in range(1, N):
        if check[i]:
            continue

        check[i] = True
        sel[depth] = i

        cost = G[sel[depth - 1]][sel[depth]]
        if cost == 0:
            return

        perm(depth + 1, acc + cost)
        check[i] = False


N = int(input())

G = [list(map(int, input().split())) for _ in range(N)]

answer = 10_000_000
check = [False] * N
sel = [0] * N

check[0] = True
sel[0] = 0

perm(1, 0)

print(answer)
