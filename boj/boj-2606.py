from collections import deque


def bfs(adj_matrix, visited, start):
    Q = deque()
    Q.appendleft(start)

    while Q:
        curr = Q.pop()
        visited[curr] = 1

        for i in range(1, len(adj_matrix)):
            if adj_matrix[curr][i] == 1 and visited[i] == 0:
                visited[i] = 1
                Q.appendleft(i)


K = int(input())
N = int(input())

visited = [0] * (K + 1)
adj_matrix = [[0] * (K + 1) for _ in range(K + 1)]

for i in range(N):
    edge = tuple(map(int, input().split()))
    adj_matrix[edge[0]][edge[1]] = 1
    adj_matrix[edge[1]][edge[0]] = 1

bfs(adj_matrix, visited, 1)

answer = sum(visited) - 1

print(answer)
