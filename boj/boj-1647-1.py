import heapq


def prim():
    dist = [1_000_000_000] * (N + 1)
    visited = set()
    heap = []
    heapq.heappush(heap, (0, 1))
    dist[0] = 0

    while heap:
        w, n = heapq.heappop(heap)

        if n in visited:
            continue

        dist[n] = w
        visited.add(n)

        for nw, nn in adj[n]:
            if nn not in visited and nw < dist[nn]:
                heapq.heappush(heap, (nw, nn))

    return sum(dist) - max(dist)


N, M = map(int, input().split())
adj = [[] for _ in range(N + 1)]

for i in range(M):
    x, y, w = map(int, input().split())
    adj[x].append((w, y))
    adj[y].append((w, x))

print(prim())
