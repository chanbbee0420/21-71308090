import sys

input = sys.stdin.readline 

n = int(input())

for i in range(n):
  ps = list(input())
  stack = []
  for j in ps:
    if j == '(':
      stack.append(j)
    elif j == ')':
      if len(stack) != 0 and stack[-1] == '(':
        stack.pop()
      else:
        stack.append(')')
        break

  if len(stack) == 0:
    print('YES')
  else:
    print('NO')