n = list(input())
rst = []

for i in n:
	if i.isupper():
		rst.append(i)

print(''.join(rst))