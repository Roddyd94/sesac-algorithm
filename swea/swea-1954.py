import sys

sys.stdin = open(f"input-{1954}.txt", "r")

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    # ///////////////////////////////////////////////////////////////////////////////////
    board_length = int(input())
    board = []

    for i in range(board_length):
        board.append([0] * board_length)

    num = 1
    depth = 0
    while depth * 2 < board_length:
        for i in range(board_length - depth * 2 - 1):
            board[depth][i + depth] = num
            num += 1
        for i in range(board_length - depth * 2 - 1):
            board[i + depth][board_length - depth - 1] = num
            num += 1
        for i in range(board_length - depth * 2 - 1):
            board[board_length - depth - 1][board_length - depth - 1 - i] = num
            num += 1
        for i in range(board_length - depth * 2 - 1):
            board[board_length - depth - 1 - i][depth] = num
            num += 1
        depth += 1

    if board_length % 2 == 1:
        board[board_length // 2][board_length // 2] = num

    print(f"#{test_case}")
    for i in range(board_length):
        print(*board[i])
    # ///////////////////////////////////////////////////////////////////////////////////
