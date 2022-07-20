import sys

input = sys.stdin.readline

n = int(input())
top = list(map(int, input().split()))
stack = []
ans = [0 for i in range(n)]

for i in range(n):
  while stack:
    if stack[-1][1] > top[i]:
      ans[i] = stack[-1][0] + 1
      break
    else:
      stack.pop()
  stack.append([i, top[i]])

print(*ans)