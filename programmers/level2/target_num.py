# BFS
# from collections import deque
# def solution(numbers, target):
#     answer = 0
#     queue = deque()
#     queue.append([numbers[0], 0])
#     queue.append([-1 * numbers[0], 0])
    
#     while queue:
#         tmp, idx = queue.popleft()
#         idx += 1
#         if idx < len(numbers):
#             queue.append([tmp + numbers[idx], idx])
#             queue.append([tmp - numbers[idx], idx])
#         else:
#             if tmp == target:
#                 answer += 1
    
#     return answer

# DFS
answer = 0
def DFS(idx, numbers, target, value):
    global answer
    N = len(numbers)
    if(idx== N and target == value):
        answer += 1
        return
    if(idx == N):
        return

    DFS(idx+1,numbers,target,value+numbers[idx])
    DFS(idx+1,numbers,target,value-numbers[idx])
def solution(numbers, target):
    global answer
    DFS(0,numbers,target,0)
    return answer