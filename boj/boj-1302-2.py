from collections import defaultdict
import sys

sys.stdin = open(f"input-{1302}.txt", "r")
# input = sys.stdin.readline

count = int(input())

book_sales = defaultdict(int)

for i in range(count):
    book = input()
    book_sales[book] += 1

book_sales = sorted(book_sales.items(), key=lambda x: (-x[1], x[0]))

best_seller = book_sales[0][0]

print(best_seller)
