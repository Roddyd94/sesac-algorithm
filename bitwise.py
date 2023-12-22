from collections import defaultdict

nums = [4, 2, 3, 1, 3, 1, 4]

"""
counter = defaultdict(int)

for n in nums:
    counter[n] += 1

for k, v in counter.items():
    if v == 1:
        print(k)
"""

"""
counter = set()

for n in nums:
    if n in counter:
        counter.remove(n)
        continue

    counter.add(n)

for n in counter:
    print(n)
"""

"""
counter = [0] * (max(nums) + 1)

for n in nums:
    counter[n] += 1

for ix in range(len(counter)):
    if counter[ix] == 1:
        print(ix)
"""


answer = 0
for n in nums:
    answer ^= n

print(answer)
