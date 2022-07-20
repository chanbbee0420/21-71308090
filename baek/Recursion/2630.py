n = int(input())
paper = [list(map(int,(input().split()))) for _ in range(n)]

# n = 8
# paper = [[1, 1, 0, 0, 0, 0, 1, 1], [1, 1, 0, 0, 0, 0, 1, 1], [0, 0, 0, 0, 1, 1, 0, 0], [0, 0, 0, 0, 1, 1, 0, 0], [1, 0, 0, 0, 1, 1, 1, 1], [0, 1, 0, 0, 1, 1, 1, 1], [0, 0, 1, 1, 1, 1, 1, 1], [0, 0, 1, 1, 1, 1, 1, 1]]

res = []

def solve(x, y, n):
  global blue_cnt, white_cnt
  color = paper[x][y]
  for i in range(x, x+n):
    for j in range(y, y+n):
      if color != paper[i][j]:
        n = n//2
        solve(x, y, n)
        solve(x, y+n, n)
        solve(x+n, y, n)
        solve(x+n, y+n, n)
        return
  if color == 0:
    res.append(0)
  if color == 1:
    res.append(1)

solve(0, 0, n)
print(res.count(0))
print(res.count(1))
