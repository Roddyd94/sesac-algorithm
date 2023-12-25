def perm(depth):
    if depth == M:
        results.append(sel.copy())
        return

    for i in range(N):
        if check[i]:
            continue

        check[i] = True
        sel[depth] = arr[i]
        perm(depth + 1)
        check[i] = False


N, M = map(int, input().split())

arr = list(map(int, input().split()))
sel = [0] * M
check = [False] * N

results = []

perm(0)

results.sort()

for result in results:
    print(*result)
