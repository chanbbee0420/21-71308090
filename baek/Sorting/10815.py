n = int(input())
cards = list(map(int, input().split()))

m = int(input())
targets = list(map(int, input().split()))

dict = {targets[i]: 0 for i in range(m)}

for i in range(n):
	if cards[i] in dict:
		dict[cards[i]] += 1

print(' '.join(map(str, list(dict.values()))))

