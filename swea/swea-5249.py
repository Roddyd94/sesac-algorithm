import sys

sys.stdin = open(f"input-{5249}.txt", "r")


T = int(input())


def make_set(x):
    p[x] = x


def find_set(x):
    if p[x] != x:
        p[x] = find_set(p[x])
    return p[x]


# def union(x, y):
#     p[find_set(y)] = find_set(x)


def union(x, y):
    link(find_set(x), find_set(y))


def link(x, y):
    if r[x] > r[y]:
        p[y] = x
    else:
        p[x] = y
        if r[x] == r[y]:
            r[y] += 1


for tc in range(1, T + 1):
    V, E = map(int, input().split())
    edges = [list(map(int, input().split())) for _ in range(E)]
    edges.sort(key=lambda x: x[2])
    p = [i for i in range(V + 1)]
    r = [0] * (V + 1)

    # for i in range(V + 1):
    #     make_set(i)

    answer = 0
    cnt = 0

    for x, y, w in edges:
        if find_set(x) != find_set(y):
            union(x, y)
            answer += w
            cnt += 1

            if cnt == V:
                break

    print(f"#{tc} {answer}")
