import sys
input = sys.stdin.readline

n = list(input().rstrip())[::-1]
def calc(x):
  r = 0
  while n:
    a = n.pop()
    if a == '(' or a == '[':
      r += calc(a)
    elif x == '(' and a == ')':
      return 2 * max(1, r)
    elif x == '[' and a == ']':
      return 3 * max(1, r)

  print(0)
  sys.exit()
  
res = 0
while n:
  res += calc(n.pop())
print(res)