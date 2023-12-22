arr = ["a", "b", "c", "d"]

"""
sel = [0] * len(arr)
check = [False] * len(arr)


def perm(depth):
    if depth == len(arr):
        print(sel)
        return

    for i in range(len(arr)):
        if not check[i]:
            check[i] = True
            sel[depth] = arr[i]
            perm(depth + 1)
            check[i] = False


perm(0)
"""

"""
sel = [0] * len(arr)


def perm(depth):
    if depth == len(arr):
        print(sel)
        return

    for i in range(len(arr)):
        sel[depth] = arr[i]
        perm(depth + 1)


perm(0)
"""
