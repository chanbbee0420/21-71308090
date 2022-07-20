n, r, c = map(int, input().split())

res = 0

def z(x, y, n):
  global res

  if x == r and y == c:
    print(res)
    exit(0)

  if n == 1:
    res += 1
    return

  if not(x<=r<x+n and y<=c<y+n):
    res += n*n
    return

  z(x, y, n//2)
  z(x, y+n//2, n//2)
  z(x+n//2, y, n//2)
  z(x+n//2, y+n//2, n//2)

z(0, 0, 2**n)
