from collections import deque
import sys

sys.stdin = open(f"input-{1226}.txt", "r")

dr = [0, 1, 0, -1]
dc = [-1, 0, 1, 0]


def bfs(map, r, c):
    Q = deque()

    Q.append((r, c))

    while Q:
        r, c = Q.popleft()

        map[r][c] = 1

        for i in range(4):
            nr, nc = r + dr[i], c + dc[i]

            if r < 0 and r >= 16 and c < 0 and c >= 16:
                continue

            if map[nr][nc] == 1:
                continue

            if map[nr][nc] == 3:
                return True

            Q.append((nr, nc))

    return False


T = 10
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for _ in range(1, T + 1):
    # ///////////////////////////////////////////////////////////////////////////////////
    test_case = int(input())
    board = [list(map(int, input())) for i in range(16)]

    found = False
    r, c = -1, -1

    for i in range(16):
        for j in range(16):
            if board[i][j] == 2:
                found = True
                r, c = i, j
                break
            if found:
                break

    answer = 1 if bfs(board, r, c) else 0

    print(f"#{test_case} {answer}")
    # ///////////////////////////////////////////////////////////////////////////////////
