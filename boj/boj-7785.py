import sys

input = sys.stdin.readline

n = int(input())

enter_log = set()

for i in range(n):
    name, state = input().split()
    if state == "enter":
        enter_log.add(name)

    if state == "leave":
        enter_log.remove(name)

enter_log = sorted(list(enter_log), reverse=True)

for name in enter_log:
    print(name)
