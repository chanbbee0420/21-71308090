a = input()
b = a.replace('>','<').split('<')
s = ""

for i in range(len(b)):
  if i%2:
    s += '<' + b[i] + '>'
  else:
    c = b[i].split()
    s += ' '.join([d[::-1] for d in c])

print(s)
