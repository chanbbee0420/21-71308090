import sys
from collections import deque


n = int(sys.stdin.readline())

queue = deque()

for i in range(n):
  cmd = sys.stdin.readline().split()

  if cmd[0] == 'push':
    queue.append(cmd[-1])

  elif cmd[0] == 'pop':
    if queue:
      print(queue.popleft())
    else:
      print(-1)

  elif cmd[0] == 'size':
    print(len(queue))

  elif cmd[0] == 'empty':
    if len(queue) == 0: 
      print(1)
    else : 
      print(0)

  elif cmd[0] == 'front':
    if len(queue) == 0:
      print(-1)
    else:
      print(queue[0])

  elif cmd[0] == 'back':
    if len(queue) == 0:
      print(-1)
    else:
      print(queue[-1])



import sys
from collections import deque

n = int(sys.stdin.readline())
que = deque()   # 빈 큐 만들기

for _ in range(n):
    command = sys.stdin.readline().split()

    if command[0] == 'push':
        que.append(command[-1])     # print(que) -> deque(['1'])
    elif command[0] == 'pop':   # 큐는 선입선출이므로 popleft() 메소드사용
        if not que:
            print(-1)
        else:
            print(que.popleft())
    elif command[0] == 'size':
        print(len(que))
    elif command[0] == 'empty':
        if not que:
            print(1)
        else:
            print(0)
    elif command[0] == 'front':  # 큐의 가장 앞 인덱스는 0
        if not que:
            print(-1)
        else:
            print(que[0])
    elif command[0] == 'back':  # 큐의 가장 마지막 인덱스는 -1
        if not que:
            print(-1)
        else:
            print(que[-1])