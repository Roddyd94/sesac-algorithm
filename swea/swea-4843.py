import sys

sys.stdin = open(f"input-{4843}.txt", "r")

T = int(input())

for test_case in range(1, T + 1):
    # ///////////////////////////////////////////////////////////////////////////////////
    N = int(input())

    nums = list(map(int, input().split()))
    nums.sort()

    answer = []
    for i in range(5):
        answer.append(nums[-1 - i])
        answer.append(nums[i])

    print(f'#{test_case}', *answer)
    # ///////////////////////////////////////////////////////////////////////////////////
