n = int(input())
books = dict()

for i in range(n):
	current = input()
	books[current] = books.get(current, 0) + 1

rst = sorted(books.items(), key=(lambda x: (-x[-1],x[0])))
print(rst[0][0])