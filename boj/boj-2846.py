n = int(input())

nums = list(map(int, input().split()))

max_bump = 0
bump = 0
for i in range(n - 1):
    if nums[i] < nums[i + 1]:
        bump += nums[i + 1] - nums[i]
        max_bump = max(max_bump, bump)
        continue

    bump = 0

print(max_bump)
