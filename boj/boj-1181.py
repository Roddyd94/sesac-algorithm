n = int(input())

words = set()
for i in range(n):
    words.add(input())

words = sorted(list(words), key=lambda x: (len(x), x))

for word in words:
    print(word)
