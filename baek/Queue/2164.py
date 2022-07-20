import sys
from collections import deque

input = sys.stdin.readline

n = int(input())
cards = deque()

for i in range(1, n+1):
  cards.append(i)

while len(cards) > 1:
  cards.popleft()
  cards.append(cards.popleft())

print(cards.pop())



# import sys 
# N = int(sys.stdin.readline()) 
# arr = [i+1 for i in range(N)] 
# while len(arr) > 1: 
#   if len(arr) % 2: 
#     t = [arr[-1]] 
#     t.extend(arr[1::2]) 
#     arr = t 
#   else: 
#     arr = arr[1::2] 

# print(arr[0])

