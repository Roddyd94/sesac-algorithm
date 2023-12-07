from typing import List
import sys

sys.stdin = open(f"input-{2630}.txt", "r")


def paper(r: int, c: int, board: List[List[int]], board_length: int):
    if board_length == 1:
        if board[r][c] == 1:
            return (0, 1)
        else:
            return (1, 0)

    nw = paper(r, c, board, board_length // 2)
    ne = paper(r, c + board_length // 2, board, board_length // 2)
    sw = paper(r + board_length // 2, c, board, board_length // 2)
    se = paper(r + board_length // 2, c + board_length // 2, board, board_length // 2)

    combined = zip(nw, ne, sw, se)
    result = tuple(map(sum, combined))

    if result[0] == 0 and result[1] == 4:
        result = (0, 1)

    if result[0] == 4 and result[1] == 0:
        result = (1, 0)

    return result


board = []
board_length = int(input())

for i in range(board_length):
    board.append(list(map(int, input().split())))

answer = paper(0, 0, board, board_length)

print(answer[0])
print(answer[1])
