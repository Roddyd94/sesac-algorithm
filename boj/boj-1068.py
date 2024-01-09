from collections import deque

N = int(input())

parents = list(map(int, input().split()))
node_to_del = int(input())
deleted = []

for i in range(N):
    if parents[i] == -1:
        root = i
        break


Q = deque()
Q.append(node_to_del)

while Q:
    curr = Q.popleft()
    parents[curr] = -2

    for i in range(N):
        if parents[i] == curr:
            Q.append(i)

answer = 0
for i in range(N):
    if i not in parents and parents[i] != -2:
        answer += 1

print(*parents)
print(answer)
