import sys

sys.stdin = open(f"input-{16268}.txt", "r")

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    # ///////////////////////////////////////////////////////////////////////////////////
    row, col = map(int, input().split())
    board = []
    answer = 0

    board.append([0] * (col + 2))
    for i in range(row):
        board.append([0] + list(map(int, input().split())) + [0])
    board.append([0] * (col + 2))

    for i in range(1, row + 1):
        for j in range(1, col + 1):
            score = sum(
                [
                    board[i][j],
                    board[i - 1][j],
                    board[i + 1][j],
                    board[i][j - 1],
                    board[i][j + 1],
                ]
            )
            answer = max(score, answer)

    print(f"#{test_case} {answer}")
    # ///////////////////////////////////////////////////////////////////////////////////
