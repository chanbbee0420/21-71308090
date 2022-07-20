n = int(input())
num_list = [list(map(int, input().split()) for _ in range(n))]
# n = 9
# num_list = [[0, 0, 0, 1, 1, 1, -1, -1, -1], [0, 0, 0, 1, 1, 1, -1, -1, -1], [0, 0, 0, 1, 1, 1, -1, -1, -1], [1, 1, 1, 0, 0, 0, 0, 0, 0], [1, 1, 1, 0, 0, 0, 0, 0, 0], [1, 1, 1, 0, 0, 0, 0, 0, 0], [0, 1, -1, 0, 1, -1, 0, 1, -1], [0, -1, 1, 0, 1, -1, 0, 1, -1], [0, 1, -1, 1, 0, -1, 0, 1, -1]]

one_count = 0
zero_count = 0
m_one_count = 0

def num_paper(x, y, n):
  global one_count, zero_count, m_one_count

  paper = num_list[x][y]
  for i in range(x, x+n):
    for j in range(y, y+n):
      if paper != num_list[i][j]:
        paper = -2
        break

  if paper == -2:
    n = n //3
    num_paper(x, y, n)
    num_paper(x+n, y, n)
    num_paper(x+2*n, y, n)
    num_paper(x, y+n, n)
    num_paper(x+n, y+n, n)
    num_paper(x+2*n, y+n, n)
    num_paper(x, y+2*n, n)
    num_paper(x+n, y+2*n, n)
    num_paper(x+2*n, y+2*n, n)
  elif paper == 1:
    one_count += 1
  elif paper == 0:
    zero_count += 1
  else:
    m_one_count += 1

num_paper(0, 0, n)
print(m_one_count)
print(zero_count)
print(one_count)




