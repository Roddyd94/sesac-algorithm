import sys

sys.stdin = open(f"input-{4880}.txt", "r")


def rock_scissor_paper(p1, p2):
    if (p1 == 1 and p2 == 2) or (p1 == 2 and p2 == 3) or (p1 == 3 and p2 == 1):
        return 1
    elif (p1 == 1 and p2 == 3) or (p1 == 2 and p2 == 1) or (p1 == 3 and p2 == 2):
        return -1
    return 0


def tornament(cards, l, r):
    if l == r:
        return l

    player1 = tornament(cards, l, (l + r) // 2)
    player2 = tornament(cards, (l + r) // 2 + 1, r)

    rsp1 = cards[player1]
    rsp2 = cards[player2]

    if rock_scissor_paper(rsp1, rsp2) == 1:
        return player2

    return player1


T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    N = int(input())

    cards = list(map(int, input().split()))

    answer = tornament(cards, 0, N - 1) + 1
    print(f"#{test_case} {answer}")
