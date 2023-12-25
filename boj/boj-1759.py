from functools import reduce


def comb(ix, six, consonant, vowel):
    if six == N:
        if consonant >= 2 and vowel >= 1:
            print(reduce(lambda x, y: x + y, sel))
        return

    if ix == M:
        return

    is_vowel = False
    if arr[ix] in ["a", "e", "i", "o", "u"]:
        is_vowel = True

    sel[six] = arr[ix]
    comb(
        ix + 1,
        six + 1,
        consonant + (0 if is_vowel else 1),
        vowel + (1 if is_vowel else 0),
    )
    comb(ix + 1, six, consonant, vowel)


N, M = map(int, input().split())

arr = input().split()
arr.sort()

sel = [0] * N

comb(0, 0, 0, 0)
