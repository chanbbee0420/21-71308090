def main():
	a, b = input().split()
	min = 50
	
	for i in range(len(b) - len(a) + 1):
		cnt = 0
		for j in range(len(a)):
			if a[j] != b[i+j]:
				cnt += 1
		if cnt < min:
			min = cnt
	
	print(min)

if __name__ == '__main__':
	main()