import sys

sys.stdin = open(f"input-{2001}.txt", "r")

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    # ///////////////////////////////////////////////////////////////////////////////////
    M, N = map(int, input().split())
    board = []
    answer = 0

    for i in range(M):
        board.append(list(map(int, input().split())))

    for i in range(M - N + 1):
        for j in range(M - N + 1):
            flies = 0

            for k in range(i, i + N):
                flies += sum(board[k][j : j + N])

            answer = max(flies, answer)

    print(f"#{test_case} {answer}")
    # ///////////////////////////////////////////////////////////////////////////////////
