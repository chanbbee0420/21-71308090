import sys
input = sys.stdin.readline

n = int(input())
que = []

for i in range(n):
  cmd = input().split()

  if cmd[0] == 'push':
    que.append(cmd[1])

  elif cmd[0] == 'pop':
    if not que:
      print(-1)
    else: 
      print(que.pop(0))

  elif cmd[0] == 'size':
    print(len(que))

  elif cmd[0] == 'empty':
    if not que:
      print(1)
    else: 
      print(0)

  elif cmd[0] == 'front':
    if not que:
      print(-1)
    else:
      print(que[0])

  elif cmd[0] == 'back':
    if not que:
      print(-1)
    else:
      print(que[-1])
