import sys

input = sys.stdin.readline

V, E = map(int, input().split())

edges = [tuple(map(int, input().split())) for _ in range(E)]
edges.sort(key=lambda x: x[2])


def kruskal():
    parents = [i for i in range(V + 1)]
    ranks = [0] * (V + 1)
    mst_weight = 0

    def find_set(x):
        if x == parents[x]:
            return parents[x]

        parents[x] = find_set(parents[x])
        return parents[x]

    def merge(x, y):
        if ranks[find_set(x)] < ranks[find_set(y)]:
            parents[find_set(x)] = y
        else:
            parents[find_set(y)] = x
            if ranks[find_set(x)] == ranks[find_set(y)]:
                ranks[find_set(x)] += 1

    for u, v, w in edges:
        if find_set(u) == find_set(v):
            continue

        mst_weight += w
        merge(u, v)

    return mst_weight


print(kruskal())
