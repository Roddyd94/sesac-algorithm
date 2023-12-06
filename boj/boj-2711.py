import sys

sys.stdin = open(f"input-{2711}.txt", "r")

cnt_word = int(input())

for i in range(cnt_word):
    ix_str, word = input().split()
    ix = int(ix_str) - 1

    answer = word[:ix] + word[ix + 1 :]

    print(answer)
