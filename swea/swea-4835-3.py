import sys

sys.stdin = open(f"input-{4835}.txt", "r")

T = int(input())

for test_case in range(1, T + 1):
    cnt, seq = map(int, input().split())
    nums = list(map(int, input().split()))

    max_sum, min_sum = 0, sum(nums)

    prefix_sum = [0]
    for i in range(cnt):
        prefix_sum.append(prefix_sum[-1] + nums[i])

    for i in range(0, cnt - seq + 1):
        temp_sum = prefix_sum[seq + i] - prefix_sum[i]
        max_sum = max(max_sum, temp_sum)
        min_sum = min(min_sum, temp_sum)

    answer = max_sum - min_sum
    print(f"#{test_case} {answer}")
