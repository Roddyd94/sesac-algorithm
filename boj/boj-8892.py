import sys
sys.stdin = open(f"input-{8892}.txt", "r")

TC = int(input())

for T in range(TC):
    num_of_words = int(input())
    words = []

    for i in range(num_of_words):
        words.append(input())
    
    found = False

    for i in range(num_of_words):
        for j in range(num_of_words):
            if words[i] == words[j]:
                continue

            if words[i] + words[j] == (words[i] + words[j])[::-1]:
                print(words[i] + words[j])
                found = True
                break

        if found:
            break
    
    if not found:
        print(0)