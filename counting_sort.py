class Ex:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __repr__(self) -> str:
        return f"({self.a}, {self.b})"


nums = [
    Ex(4, 1),
    Ex(4, 2),
    Ex(2, 1),
    Ex(3, 1),
    Ex(5, 1),
    Ex(5, 2),
    Ex(1, 1),
    Ex(1, 2),
    Ex(5, 3),
]

counts = [0] * (5 + 1)
sorted_nums = [0] * len(nums)

for num in nums:
    counts[num.a] += 1

for i in range(1, len(counts)):
    counts[i] = counts[i] + counts[i - 1]

for j in range(len(nums) - 1, -1, -1):
    sorted_nums[counts[nums[j].a] - 1] = nums[j]
    counts[nums[j].a] -= 1

# for j in range(len(nums)):
#     sorted_nums[counts[nums[j].a - 1]] = nums[j]
#     counts[nums[j].a - 1] += 1

print(sorted_nums)
