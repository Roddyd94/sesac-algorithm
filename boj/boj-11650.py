N = int(input())

dots = []
for i in range(N):
    dots.append(list(map(int, input().split())))

dots = sorted(dots, key=lambda x: (x[0], x[1]))

for i in range(N):
    print(*dots[i])