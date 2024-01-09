from heapq import heappush as hpush, heappop as hpop
import sys

input = sys.stdin.readline

N = int(input())

lectures = [tuple(map(int, input().split())) for _ in range(N)]
heap = []

lectures.sort(key=lambda x: (x[0], x[1]))

for s, t in lectures:
    if heap:
        e = hpop(heap)

        if s < e:
            hpush(heap, e)

    hpush(heap, t)

print(len(heap))
