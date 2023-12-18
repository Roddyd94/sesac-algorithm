import sys

sys.stdin = open(f"input-{1974}.txt", "r")


def check_row(board):
    for row in board:
        if len(set(row)) != 9:
            return False

    return True


def check_col(board):
    board = list(zip(*board))

    return check_row(board)


def check_nine(board):
    board_alt = []
    for i in range(0, 9, 3):
        for j in range(0, 9, 3):
            board_alt.append(
                [board[m][n] for m in range(i, i + 3) for n in range(j, j + 3)]
            )
    return check_row(board_alt)


T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    # ///////////////////////////////////////////////////////////////////////////////////
    board = []

    for i in range(9):
        board.append(list(map(int, input().split())))

    answer = 1

    if not check_row(board):
        answer = 0
    if not check_col(board):
        answer = 0
    if not check_nine(board):
        answer = 0

    print(f"#{test_case} {answer}")
    # ///////////////////////////////////////////////////////////////////////////////////
