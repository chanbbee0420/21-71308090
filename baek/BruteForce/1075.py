n = input()
f = int(input())
x = int(n[:-2] + '00')
while True:
    if x % f == 0:
        break
    x += 1
print(str(x)[-2:])
