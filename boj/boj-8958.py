import sys

sys.stdin = open(f"input-{8958}.txt", "r")

cnt_quiz = int(input())

for i in range(cnt_quiz):
    quiz = input()
    score = 0
    combo = 1

    for quiz_result in quiz:
        if quiz_result == "O":
            score += combo
            combo += 1
        else:
            combo = 1

    print(score)
