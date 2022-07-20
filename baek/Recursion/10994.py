n = int(input())
stars = [[' ' for _ in range(4 * n - 3)] for _ in range(4 * n - 3)]

def print_star(x, y, n):
  if n == 1:
    stars[y][x] = '*'
    return

  length = 4 * n - 3
  for i in range(length):
    stars[y][x+i] = '*'
    stars[y+i][x] = '*'
    stars[y+length-1][x+i] = '*'
    stars[y+i][x+length-1] = '*'

  print_star(x+2, y+2, n-1)

print_star(0, 0, n)

for star in stars:
  print(''.join(star))