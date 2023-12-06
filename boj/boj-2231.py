target = int(input())

answer = max(target - 54, 1)

found = False

while answer < target:
    number = str(answer)
    temp = answer

    for c in number:
        temp += int(c)

    if temp == target:
        print(answer)
        found = True
        break

    answer += 1

if not found:
    print(0)
