from itertools import combinations, permutations

arr = ["a", "b", "c", "d", "e"]

"""
for i in range(len(arr)):
    for j in range(i + 1, len(arr)):
        print(arr[i], arr[j])
"""

"""
for i in range(len(arr)):
    for j in range(i, len(arr)):
        print(arr[i], arr[j])
"""

"""
for x, y in combinations(arr, 2):
    print(x, y)
"""

"""
for x, y in permutations(arr, 2):
    print(x, y)
"""

sel = [0, 0]

"""
def combination(idx, sidx):
    if sidx == len(sel):
        print(sel)
        return

    if idx == len(arr):
        return

    sel[sidx] = arr[idx]
    combination(idx + 1, sidx + 1)
    combination(idx + 1, sidx)


combination(0, 0)
"""


def combination(idx, sidx):
    if sidx == len(sel):
        print(sel)
        return

    if idx == len(arr):
        return

    sel[sidx] = arr[idx]
    combination(idx, sidx + 1)
    combination(idx + 1, sidx)


combination(0, 0)
