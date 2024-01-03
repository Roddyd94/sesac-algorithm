import sys

input = sys.stdin.readline


def order(root):
    S = []
    S.append(root)
    visited[root] = True

    while S:
        parent = S.pop()

        for child in G[parent]:
            if visited[child]:
                continue

            parents[child] = parent
            S.append(child)
            visited[child] = True


N = int(input())

G = [[] for _ in range(N + 1)]
parents = [0] * (N + 1)
visited = [False] * (N + 1)

root = 1
visited[1] = True

for _ in range(N - 1):
    n1, n2 = map(int, input().split())
    G[n1].append(n2)
    G[n2].append(n1)

order(root)

for i in range(2, N + 1):
    print(parents[i])
