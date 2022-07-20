import sys

input = sys.stdin.readline

n = int(input())
n_lst = sorted(list(map(int,input().split())))
m = int(input())
target = list(map(int,input().split()))

def binary_search(target):
  left = 0
  right = n - 1

  while left <= right:
    mid = (left + right) // 2
    if n_lst[mid] == target:
      return True

    if target < n_lst[mid]:
      right = mid - 1
    elif target > n_lst[mid]:
      left = mid + 1

for i in range(m):
  if binary_search(target[i]):
    print(1)
  else:
    print(0)