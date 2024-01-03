import sys

input = sys.stdin.readline

N = int(input())

s = 0

for _ in range(N):
    operation = input().split()
    if len(operation) == 1:
        match operation[0]:
            case "all":
                s = 2**20 - 1
            case "empty":
                s = 0
    else:
        operand = int(operation[1])
        match operation[0]:
            case "add":
                s |= 1 << (operand - 1)
            case "remove":
                s &= ~(1 << (operand - 1))
            case "toggle":
                s ^= 1 << (operand - 1)
            case "check":
                if s & (1 << (operand - 1)):
                    print(1)
                else:
                    print(0)
