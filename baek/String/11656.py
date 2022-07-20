n = list(input())
strs = []

for i in range(len(n)):
	strs.append(''.join(n[i:]))

strs.sort()
print(*strs)