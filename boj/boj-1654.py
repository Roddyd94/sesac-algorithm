K, N = map(int, input().split())


def b_search(lines, l, r, target):
    if l > r:
        return r

    c = (l + r) // 2
    count = 0

    for line in lines:
        count += line // c

    if target <= count:
        return b_search(lines, c + 1, r, target)
    else:
        return b_search(lines, l, c - 1, target)


lines = []
for i in range(K):
    lines.append(int(input()))

answer = b_search(lines, 1, max(lines), N)

print(answer)
