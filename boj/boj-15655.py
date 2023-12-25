def perm(depth):
    if depth == M:
        if sel == sorted(sel, key=lambda x: x):
            print(*sel)
        return

    for i in range(N):
        if check[i]:
            continue

        check[i] = True
        sel[depth] = arr[i]
        perm(depth + 1)
        check[i] = False


N, M = map(int, input().split())

check = [False] * N
sel = [0] * M
arr = list(map(int, input().split()))
arr.sort()

perm(0)
