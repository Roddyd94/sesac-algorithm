T = int(input())

for tc in range(T):
    vps = input()
    check = []
    answer = True

    for ch in vps:
        if ch == "(":
            check.append(1)
            continue

        if check:
            check.pop()
            continue

        answer = False
        break

    if check:
        answer = False

    print("YES" if answer else "NO")
