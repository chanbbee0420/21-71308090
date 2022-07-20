n = list(input())
stack = []
# n = ['(',')','(','(','(','(',')','(',')',')','(','(',')',')','(',')',')',')','(','(',')',')']
cnt = 0

for i in range(len(n)):
  if n[i] == '(':
    stack.append('(')

  else:
    if n[i-1] == '(':
      stack.pop()
      cnt += len(stack)
    else:
      stack.pop()
      cnt += 1


print(cnt)