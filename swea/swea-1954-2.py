import sys

sys.stdin = open(f"input-{1954}.txt", "r")

dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    # ///////////////////////////////////////////////////////////////////////////////////
    board_length = int(input())
    board = []

    for i in range(board_length):
        board.append([0] * board_length)

    num = 1
    r, c, dix = 0, 0, 0

    while num <= board_length**2:
        board[r][c] = num
        num += 1

        nr = r + dr[dix]
        nc = c + dc[dix]

        if (
            nr >= board_length
            or nr < 0
            or nc >= board_length
            or nc < 0
            or board[nr][nc] != 0
        ):
            dix = (dix + 1) % 4
            nr = r + dr[dix]
            nc = c + dc[dix]

        r = nr
        c = nc

    print(f"#{test_case}")
    for i in range(board_length):
        print(*board[i])
    # ///////////////////////////////////////////////////////////////////////////////////
