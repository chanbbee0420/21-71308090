import sys

input = sys.stdin.readline
n, w ,L = map(int, input().split())
trucks = list(map(int, input().split()))

bridge = [0] * w
t = 0
weight = 0

while True:
  out = bridge.pop(0)
  weight -= out

  if trucks:
    if weight + trucks[0] <= L:
      bridge.append(trucks[0])
      weight += trucks[0]
      trucks.pop(0)
    else:
      bridge.append(0)

  t += 1

  if not bridge:
    break

print(t)