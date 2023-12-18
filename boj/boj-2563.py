N = int(input())

board = []
for i in range(100):
    board.append([0] * 100)

answer = 0

for i in range(N):
    x, y = map(int, input().split())
    for m in range(x - 1, x + 9):
        for n in range(y - 1, y + 9):
            if board[m][n] != 0:
                continue

            board[m][n] = 1
            answer += 1

print(answer)
