strs = input()
banned = input()

# strs = "mirkovC4nizCC44"
# banned = "C4"

# strs = "12ab112ab2ab"
# banned = "12ab"

lastChar = banned[-1]
stack = []

for char in strs:
  stack.append(char)
  if char == lastChar and ''.join(stack[-len(banned):]) == banned:
    del stack[-len(banned):]

res = ''.join(stack)

if res:
  print(res)
else:
  print("FRULA")





# lastChar = banned[-1]
# stack = []
# length = len(banned)

# for char in strs:
#     stack.append(char)
#     if char == lastChar and ''.join(stack[-length:]) == banned:
#         del stack[-length:]

# answer = ''.join(stack)

# if answer:
#   print(answer)
# else:
#   print("FRULA")

# if answer == '':
#     print("FRULA")
# else:
#     print(answer)