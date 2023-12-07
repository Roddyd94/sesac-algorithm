import sys

sys.stdin = open(f"input-{1931}.txt", "r")
input = sys.stdin.readline

N = int(input())

meetings = []
for i in range(N):
    meetings.append(list(map(int, input().split())))

meetings = sorted(meetings, key=lambda x: (x[1], x[0]))

answer = 0
last = 0
for i in range(N):
    if meetings[i][0] >= last:
        answer += 1
        last = meetings[i][1]

print(answer)
