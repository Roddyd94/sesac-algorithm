import heapq

arr = [2,4,7,3,5,8]
heapq.heapify(arr)
print(arr)

heap = []
heapq.heappush(heap, 8)
heapq.heappush(heap, 5)
heapq.heappush(heap, 3)
heapq.heappush(heap, 6)
print(heap)

