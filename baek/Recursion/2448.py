n = int(input())
star = [[' ' for _ in range(2 * n)] for _ in range(n)]


def print_star(x, y, n):
    if n == 3:
        star[x][y] = '*'
        star[x + 1][y - 1] = star[x + 1][y + 1] = '*'
        for i in range(-2, 3):
            star[x + 2][y + i] = '*'
    else:
      new_n = n // 2
      print_star(x, y, new_n)
      print_star(x + new_n, y - new_n, new_n)
      print_star(x + new_n, y + new_n, new_n)


print_star(0, n - 1, n)
for i in star:
    print("".join(i))