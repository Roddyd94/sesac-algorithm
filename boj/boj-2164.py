N = int(input())

answer = 1

while answer < N:
    answer *= 2

answer = answer - 2 * (answer - N)

print(answer)


"""
1   1
2   2
3   2
4   4
5   2
6   4
7   6
8   8
9   2
10  4
11  6
12  8
13  
"""
