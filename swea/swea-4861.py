import sys

sys.stdin = open(f"input-{4861}.txt", "r")

T = int(input())

for test_case in range(1, T + 1):
    N, M = map(int, input().split())
    board = []

    for i in range(N):
        board.append(input())

    for i in range(N):
        for j in range(N - M + 1):
            word = board[i][j : j + M]
            if word == word[::-1]:
                print(f"#{test_case} {word}")

    for i in range(N):
        for j in range(N - M + 1):
            word = ""
            for k in range(M):
                word += board[j + k][i]
            if word == word[::-1]:
                print(f"#{test_case} {word}")
