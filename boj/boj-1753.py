from collections import defaultdict
from heapq import heappush, heappop
import sys

input = sys.stdin.readline

V, E = map(int, input().split())
S = int(input())

distances = [defaultdict() for i in range(V + 1)]
for i in range(V + 1):
    distances[i][i] = 0

for _ in range(E):
    u, v, w = map(int, input().split())

    if v not in distances[u]:
        distances[u][v] = w
        continue

    distances[u][v] = min(w, distances[u][v])


def dijkstra(start):
    heap = []
    visited = [False] * (V + 1)

    def hpush(x):
        heappush(heap, x)

    def hpop():
        return heappop(heap)

    hpush((0, start))

    while heap:
        distance, u = hpop()
        visited[u] = True

        for v, w in distances[u].items():
            if visited[v]:
                continue

            if u == start:
                hpush((distance + w, v))
                continue

            if v not in distances[start] or distances[start][v] > distance + w:
                distances[start][v] = distance + w
                hpush((distance + w, v))


dijkstra(S)

for i in range(1, V + 1):
    if i not in distances[S]:
        print("INF")
        continue
    print(distances[S][i])
