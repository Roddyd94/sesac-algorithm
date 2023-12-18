N = int(input())

people = [tuple(map(int, input().split())) for _ in range(N)]
answer = []

for i in range(N):
    answer.append(1)

    for j in range(N):
        if i == j:
            continue

        if people[i][0] < people[j][0] and people[i][1] < people[j][1]:
            answer[i] += 1

print(*answer)
