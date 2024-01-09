import sys

sys.stdin = open(f"input-{5176}.txt", "r")


T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for tc in range(1, T + 1):
    N = int(input())

    binary_tree = [0] * (N + 1)
    cnt = 0

    def inorder(n):
        global cnt
        if n > N:
            return
        inorder(2 * n)
        cnt += 1
        binary_tree[n] = cnt
        inorder(2 * n + 1)

    inorder(1)

    print(f"#{tc} {binary_tree[1]} {binary_tree[N//2]}")
