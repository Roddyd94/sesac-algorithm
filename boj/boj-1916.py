import heapq
import sys

input = sys.stdin.readline


def dijkstra(start, end):
    visited = set()
    heap = []
    heapq.heappush(heap, (0, start))

    while heap:
        distance, node = heapq.heappop(heap)

        if node in visited:
            continue

        distances[node] = distance
        visited.add(node)

        for d, dest in adj[node]:
            if dest in visited:
                continue

            if distances[dest] > d + distance:
                heapq.heappush(heap, (d + distance, dest))

    return distances[end]


N = int(input())
M = int(input())

distances = [1_000_000_000] * (N + 1)
adj = [[] for _ in range(N + 1)]
for i in range(M):
    s, e, w = map(int, input().split())
    adj[s].append((w, e))

start, end = map(int, input().split())


print(dijkstra(start, end))
