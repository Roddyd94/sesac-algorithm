import sys

sys.stdin = open(f"input-{1247}.txt", "r")


def perm(depth, acc, prev):
    global answer
    if depth == N:
        acc += abs(home[0] - prev[0]) + abs(home[1] - prev[1])
        answer = min(acc, answer)
        return

    for i in range(N):
        if check[i]:
            continue

        check[i] = True
        delta = abs(targets[i][0] - prev[0]) + abs(targets[i][1] - prev[1])
        perm(depth + 1, acc + delta, targets[i])
        check[i] = False


T = int(input())
for test_case in range(1, T + 1):
    answer = 2000
    N = int(input())
    input_list = list(map(int, input().split()))

    company = tuple(input_list[0:2])
    home = tuple(input_list[2:4])
    check = [False] * N
    targets = [tuple(input_list[(2 * i) : (2 * (i + 1))]) for i in range(2, 2 + N)]

    perm(0, 0, company)

    print(f"#{test_case} {answer}")
