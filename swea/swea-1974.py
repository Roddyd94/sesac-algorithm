from typing import List
import sys

sys.stdin = open(f"input-{1974}.txt", "r")


def check_row(board: List[List[int]]):
    for i in range(9):
        num_check = set()
        for j in range(9):
            if board[i][j] not in num_check:
                num_check.add(board[i][j])
            else:
                return False

    return True


def check_col(board: List[List[int]]):
    for i in range(9):
        num_check = set()
        for j in range(9):
            if board[j][i] not in num_check:
                num_check.add(board[j][i])
            else:
                return False

    return True


def check_nine(board: List[List[int]]):
    for i in range(3):
        for j in range(3):
            num_check = set()

            for m in range(3):
                for n in range(3):
                    if board[3 * i + m][3 * j + n] not in num_check:
                        num_check.add(board[3 * i + m][3 * j + n])
                    else:
                        return False

    return True


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
