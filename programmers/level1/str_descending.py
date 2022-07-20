def solution(s):
    return ''.join(sorted(s, reverse=True))

# def solution(s):
#     s = list(s)
#     s1 = []
#     s2 = []
#     for i in range(len(s)):
#         if s[i].islower():
#             s1.append(s[i])
#         else:
#             s2.append(s[i])
            
#     s1.sort(reverse=True)
#     s2.sort(reverse=True)
    
#     return ''.join(s1 + s2)