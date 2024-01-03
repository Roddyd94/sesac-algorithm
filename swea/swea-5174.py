import sys

sys.stdin = open(f"input-{5174}.txt", "r")


def inorder(node):
    global answer

    if node == 0:
        return
    if left[node] != 0:
        inorder(left[node])
    answer += 1
    if right[node] != 0:
        inorder(right[node])


T = int(input())
for test_case in range(1, T + 1):
    E, N = map(int, input().split())
    edges = list(map(int, input().split()))

    ancestor = [0] * (E + 2)
    left = [0] * (E + 2)
    right = [0] * (E + 2)

    for i in range(E):
        parent, child = edges[2 * i : 2 * i + 2]
        if not left[parent]:
            left[parent] = child
        else:
            right[parent] = child

        ancestor[child] = parent

    answer = 0
    inorder(N)

    print(f"#{test_case} {answer}")
