import sys

n = int(sys.stdin.readline())
books = dict()
for _ in range(n):
    book = sys.stdin.readline().strip()
    if book in books:
        books[book]+=1
    else:
        books[book] = 1

max = 0
for title,num in books.items():
    if num>max:
        best_seller = title
        max = num
    elif num==max:
        best_seller= min(title,best_seller)
        
print(best_seller)