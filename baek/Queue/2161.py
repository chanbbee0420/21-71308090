import sys
from collections import deque

input = sys.stdin.readline

n = int(input())
cards = deque()
dumped = []

for i in range(1, n+1):
  cards.append(i)

while len(cards) > 1:
  dumped.append(cards.popleft())
  cards.append(cards.popleft())

dumped.append(cards.pop())
for i in dumped:
  print(i, end=' ')