import sys

input = sys.stdin.readline

t = int(input())
flag = False

for _ in range(t):
	n = int(input())
	num_list = list(input().rstrip() for _ in range(n))
	num_list.sort()
	
	for i in range(len(num_list) - 1):
		if num_list[i] in num_list[i+1][:len(num_list[i])]:
			print("NO")
			flag = True
			break

	if flag == False:
		print("YES")

	flag = False