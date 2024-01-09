import sys

input = sys.stdin.readline

def find_set(x):
    if p[x] != x:
        p[x] = find_set(p[x])
    return p[x]


def union(x, y):
    a = find_set(x)
    b = find_set(y)

    if r[a] > r[b]:
        p[b] = a
    else:
        p[a] = b
        if r[a] == r[b]:
            r[b] += 1


N, M = map(int, input().split())

edges = [list(map(int, input().split())) for _ in range(M)]
edges.sort(key=lambda x: x[2])

p = [i for i in range(N + 1)]
r = [0] * (N + 1)

answer = 0
last_weight = 0
cnt = 0

for x, y, w in edges:
    if find_set(x) == find_set(y):
        continue

    union(x, y)
    answer += w
    last_weight = w
    cnt += 1

    if cnt == N:
        break

answer -= last_weight

print(answer)
