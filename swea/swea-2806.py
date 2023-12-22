import sys

sys.stdin = open(f"input-{2806}.txt", "r")


def perm(depth):
    global answer

    if depth == N:
        answer += 1
        return

    for i in range(N):
        if check[i]:
            continue

        check_diag = False
        for j in range(depth):
            if abs(sel[j] - i) == depth - j:
                check_diag = True
                break

        if check_diag:
            continue

        check[i] = True
        sel[depth] = i
        perm(depth + 1)
        check[i] = False


T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    N = int(input())

    answer = 0
    sel = [0] * N
    check = [False] * N

    perm(0)

    print(f"#{test_case} {answer}")
