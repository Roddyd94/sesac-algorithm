import sys

sys.stdin = open(f"input-{1859}.txt", "r")

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    # ///////////////////////////////////////////////////////////////////////////////////
    cnt = int(input())
    arr = list(map(int, input().split()))
    ix = len(arr) - 1
    answer = 0

    while ix >= 0:
        highest = arr[ix]
        target_ix = ix

        cost = 0

        for i in range(ix, -1, -1):
            if arr[i] > highest:
                highest = arr[i]
                target_ix = i

        for i in range(target_ix):
            cost += arr[i]

        answer += target_ix * arr[target_ix] - cost

        arr = arr[target_ix + 1 :]
        ix = len(arr) - 1

    print(f"#{test_case} {answer}")
    # ///////////////////////////////////////////////////////////////////////////////////
