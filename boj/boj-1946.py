import sys

input = sys.stdin.readline

T = int(input())

for tc in range(T):
    N = int(input())

    answer = 0
    applicants = []
    for i in range(N):
        applicants.append(list(map(int, input().split())))

    applicants = sorted(applicants, key=lambda x: x[0])
    compare = applicants[0][:]
    answer += 1

    for i in range(1, N):
        if applicants[i][1] < compare[1]:
            answer += 1
            compare = applicants[i][:]
            
    print(answer)

