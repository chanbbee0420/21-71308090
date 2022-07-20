def toWeirdCase(s):
    return " ".join(map(lambda x: "".join([a.lower() if i % 2 else a.upper() for i, a in enumerate(x)]), s.split(" ")))


# def toWeirdCase(s):
#     return ' '.join([''.join([c.upper() if i % 2 == 0 else c.lower() for i, c in enumerate(w)]) for w in s.split()])




# def solution(s):
#     answer = ''
#     words = s.split(" ")
#     for i in words:
#         for j in range(len(i)):
#             if j % 2 == 0:
#                 answer += i[j].upper()
#             else:
#                 answer += i[j].lower()
#         answer += ' '
#     return answer[0 : -1]