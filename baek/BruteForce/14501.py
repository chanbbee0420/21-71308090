n = int(input())
t = [0] * (n+1)
p = [0] * (n+1)
ans = 0

for i in range(1, n+1):
  t[i], p[i] = map(int, input().split())

def counsel(day, profit):
  global ans

  if day == n+1:
    ans = max(profit, ans)
    return
  
  if day > n+1:
    return

  counsel(day+t[day], profit+p[day])
  counsel(day+1, profit)

counsel(1, 0)
print(ans)