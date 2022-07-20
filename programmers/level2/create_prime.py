def solution(nums):
    cnt = 0
    prime = [True] * 3000

    for i in range(2, 3000//2):
        if prime[i] == True:
            for j in range(i + i, 3000, i):
                prime[j] = False
    
    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            for k in range(j+1, len(nums)):
                tmp = nums[i] + nums[j] + nums[k]
                if prime[tmp] == True:
                    cnt += 1
                    
    return cnt




# def solution(nums):
#     from itertools import combinations as cb
#     answer = 0
#     for a in cb(nums, 3):
#         cand = sum(a)
#         for j in range(2, cand):
#             if cand%j==0:
#                 break
#         else:
#             answer += 1
#     return answer