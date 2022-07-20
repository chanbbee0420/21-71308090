def solution(A, B):
    A.sort(reverse=True)
    B.sort(reverse=True)
    res = 0
    
    for i in A:
        if i < B[0]:
            res += 1
            del B[0]
        else:
            continue
            
    return res



# from collections import deque
# def solution(A, B):
#     answer = 0
#     A.sort()
#     B.sort()
#     A = deque(A)
#     B = deque(B)
#     while A:
#         if A[-1]<B[-1]:
#             answer+=1
#             A.pop()
#             B.pop()
#         else:
#             A.pop()
#             B.popleft()

#     return answer