# 1
# from collections import Counter
# import math

# def solution(progresses, speeds):
#     days = [math.ceil((100 - a) / b) for a, b in zip(progresses, speeds)]

#     for i in range(len(days)-1):
#         if days[i] > days[i+1]:
#             days[i+1] = days[i]
            
#     cnt = Counter(days)
#     return list(cnt.values())

# 2
def solution(progresses, speeds):
    Q=[]
    for p, s in zip(progresses, speeds):
        if len(Q)==0 or Q[-1][0]<-((p-100)//s):
            Q.append([-((p-100)//s),1])
        else:
            Q[-1][1]+=1
    return [q[1] for q in Q]




# 3
def func_dev(progresses, speeds):
    answer = []
    time = 0
    count = 0
    
    while len(progresses)> 0:
        if (progresses[0] + time*speeds[0]) >= 100: 
            progresses.pop(0)
            speeds.pop(0)
            count += 1
            
        else:
            if count > 0:
                answer.append(count)
                count = 0
            time += 1
    answer.append(count)
    return answer