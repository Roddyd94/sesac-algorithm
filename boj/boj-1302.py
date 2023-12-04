import sys
sys.stdin = open(f"input-{1302}.txt", "r")

count = int(input())

book_sales = {}

for i in range(count):
    book = input()

    if book not in book_sales:
        book_sales[book] = 1
    else:
        book_sales[book] += 1

best_seller = ''
best_sold = 0
for book in book_sales.keys():
    if book_sales[book] == best_sold and book < best_seller:
        best_seller = book
    if book_sales[book] > best_sold:
        best_sold = book_sales[book]
        best_seller = book

print(best_seller)