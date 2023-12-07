import sys

sys.stdin = open(f"input-{4839}.txt", "r")

T = int(input())

for test_case in range(1, T + 1):
    # ///////////////////////////////////////////////////////////////////////////////////
    P, A, B = map(int, input().split())

    tries_A = 0
    tries_B = 0

    tries_A = b_search(1, P, A, 0)
    tries_B = b_search(1, P, B, 0)

    answer = 0 if tries_A == tries_B else ("A" if tries_A < tries_B else "B")

    print(f"#{test_case} {answer}")
    # ///////////////////////////////////////////////////////////////////////////////////


def b_search(l, r, c, tries):
    m = (l + r) // 2
    tries += 1

    if m == c:
        return tries
    elif c < m:
        return b_search(l, m, c, tries)
    else:
        return b_search(m, r, c, tries)
