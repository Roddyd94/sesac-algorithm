from heapq import heappush, heappop
import sys

input = sys.stdin.readline

V, E = map(int, input().split())

adj = [[] for _ in range(V + 1)]

for _ in range(E):
    u, v, w = map(int, input().split())
    adj[u].append((v, w))
    adj[v].append((u, w))


def prim():
    dist = [2_147_483_647] * (V + 1)
    visited = [False] * (V + 1)
    heap = []

    dist[0] = 0

    def hpush(x):
        heappush(heap, x)

    def hpop():
        return heappop(heap)

    hpush((0, 1))
    dist[1] = 0

    while heap:
        distance, u = hpop()
        visited[u] = True

        for v, w in adj[u]:
            if visited[v]:
                continue

            if dist[v] > w:
                dist[v] = w
                hpush((w, v))

    return sum(dist)


print(prim())
