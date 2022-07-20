lst = [int(input()) for i in range(9)]
# lst = [20, 7 , 23, 19, 10, 15, 25, 8, 13]
total = sum(lst)

for i in range(9):
  for j in range(i+1, 9):
    if 100 == total - (lst[i] + lst[j]): 
      num1, num2 = lst[i], lst[j]

      lst.remove(num1)
      lst.remove(num2)
      lst.sort()

      for k in range(len(lst)):
        print(lst[k])
      break

  if len(lst) < 9:
    break


