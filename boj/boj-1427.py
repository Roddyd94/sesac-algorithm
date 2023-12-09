from functools import reduce

N = input()

nums = list(N)
nums.sort(reverse=True)

number = reduce(lambda x, y: x + y, nums)

print(number)