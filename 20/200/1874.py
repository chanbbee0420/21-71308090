import sys

input = sys.stdin.readline 

n = int(input())
stack = []
res = []
cnt = 1
temp = True

for i in range(n):
  num = int(input())
  while cnt <= num:
    stack.append(cnt)
    res.append('+')
    cnt += 1
  if stack[-1] == num:
    stack.pop()
    res.append('-')
  else:
    temp = False

if temp == False:
  print('NO')
else:
  for i in res:
    print(i)
