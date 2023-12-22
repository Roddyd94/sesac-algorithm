def perm(depth):
    global answer

    if depth == N:
        answer += 1
        return

    for i in range(N):
        if check[i] or check_ld[i - depth] or check_rd[i + depth]:
            continue

        check[i] = True
        check_ld[i - depth] = True
        check_rd[i + depth] = True
        sel[depth] = i
        perm(depth + 1)
        check_rd[i + depth] = False
        check_ld[i - depth] = False
        check[i] = False


N = int(input())

answer = 0
sel = [0] * N
check = [False] * N
check_ld = [False] * (2 * N - 1)
check_rd = [False] * (2 * N - 1)

perm(0)

print(answer)
