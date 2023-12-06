from itertools import permutations, combinations
import sys

sys.stdin = open(f"input-{8892}.txt", "r")

TC = int(input())

for T in range(TC):
    num_of_words = int(input())
    words = []

    for i in range(num_of_words):
        words.append(input())

    found = False

    matching_words = list(permutations(words, 2))

    for matching_word in matching_words:
        word = matching_word[0] + matching_word[1]

        if word == word[::-1]:
            print(word)
            found = True
            break

        if found:
            break

    if not found:
        print(0)
