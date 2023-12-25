import sys

sys.stdin = open(f"input-{5209}.txt", "r")


def perm(depth, acc):
    global answer
    if depth == N:
        answer = min(answer, acc)
        return

    for i in range(N):
        if board[depth][i] + acc > answer:
            continue

        if check[i]:
            continue

        check[i] = True
        perm(depth + 1, acc + board[depth][i])
        check[i] = False


T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    answer = 1500

    N = int(input())
    board = [list(map(int, input().split())) for _ in range(N)]
    check = [False] * N

    perm(0, 0)

    print(f"#{test_case} {answer}")
