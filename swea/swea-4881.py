import sys

sys.stdin = open(f"input-{4881}.txt", "r")


def perm(depth, acc):
    global s

    if depth == N:
        s = min(s, acc)
        return acc

    if acc > s:
        return s

    for i in range(N):
        if check[i]:
            continue

        check[i] = True
        sel[depth] = arr[depth][i]
        perm(depth + 1, acc + sel[depth])
        check[i] = False

    return s


T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    N = int(input())

    arr = [list(map(int, input().split())) for _ in range(N)]
    sel = [0] * N
    check = [False] * N

    s = 10_000_000

    depth = 0

    answer = perm(depth, 0)

    print(f"#{test_case} {answer}")
