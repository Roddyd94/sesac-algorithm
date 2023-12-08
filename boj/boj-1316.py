n = int(input())


answer = 0
for i in range(n):
    word = input()
    alphabet_used = set()

    is_group_word = True
    prev = word[0]
    alphabet_used.add(prev)
    for j in range(1, len(word)):
        if word[j] == prev:
            continue

        if word[j] in alphabet_used:
            is_group_word = False
            break

        alphabet_used.add(word[j])
        prev = word[j]

    if is_group_word:
        answer += 1

print(answer)
