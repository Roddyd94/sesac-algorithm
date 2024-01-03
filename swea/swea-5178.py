import sys

sys.stdin = open(f"input-{5178}.txt", "r")


def postorder(node):
    if tree[node] != 0:
        return tree[node]

    tree[node] = postorder(node * 2) + postorder(node * 2 + 1)
    return tree[node]


T = int(input())
for test_case in range(1, T + 1):
    N, M, L = map(int, input().split())

    tree = [0] * (N + 1)

    for i in range(M):
        node, value = map(int, input().split())
        tree[node] = value

    postorder(1)
    answer = tree[L]

    print(f"#{test_case} {answer}")
