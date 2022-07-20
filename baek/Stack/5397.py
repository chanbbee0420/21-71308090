import sys

input = sys.stdin.readline

T = int(input())
stack1 = []
stack2 = []

for _ in range(T):
  case = input().strip()
  stack1 = []
  stack2 = []
  for i in case:
    if i == '<':
      if stack1:
        stack2.append(stack1.pop())
    elif i == '>':
      if stack2:
        stack1.append(stack2.pop())
    elif i == '-':
      if stack1:
        stack1.pop()
    else:
      stack1.append(i)

  stack1.extend(reversed(stack2))
  print(''.join(stack1))
