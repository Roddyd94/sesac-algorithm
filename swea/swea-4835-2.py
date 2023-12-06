import sys

sys.stdin = open(f"input-{4835}.txt", "r")

T = int(input())

for test_case in range(1, T + 1):
    # ///////////////////////////////////////////////////////////////////////////////////
    cnt, seq = map(int, input().split())
    nums = list(map(int, input().split()))

    sum_window = sum(nums[0:seq])
    max_sum, min_sum = sum_window, sum_window

    for i in range(cnt - seq):
        sum_window = sum_window + nums[seq + i] - nums[i]
        max_sum = max(max_sum, sum_window)
        min_sum = min(min_sum, sum_window)

    answer = max_sum - min_sum
    print(f"#{test_case} {answer}")
    # ///////////////////////////////////////////////////////////////////////////////////
