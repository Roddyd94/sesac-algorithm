from heapq import heappush, heappop
import sys

input = sys.stdin.readline

V, E = map(int, input().split())
S = int(input())

distances = [200_001] * (V + 1)
adj = [[] for _ in range(V + 1)]

for _ in range(E):
    u, v, w = map(int, input().split())

    adj[u].append((v, w))


def dijkstra(start):
    heap = []
    visited = [False] * (V + 1)

    def hpush(x):
        heappush(heap, x)

    def hpop():
        return heappop(heap)

    hpush((0, start))
    distances[start] = 0

    while heap:
        distance, u = hpop()
        visited[u] = True

        for v, w in adj[u]:
            if visited[v]:
                continue

            if distances[v] > distance + w:
                distances[v] = distance + w
                hpush((distance + w, v))


dijkstra(S)

for i in range(1, V + 1):
    if distances[i] == 200_001:
        print("INF")
        continue
    print(distances[i])
