def solution(answers):
    ans = []
    res = [0, 0, 0]
    s1 = [1, 2, 3, 4, 5]
    s2 = [2, 1, 2, 3, 2, 4, 2, 5]
    s3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    
    for i in range(len(answers)):
        if answers[i] == s1[i % len(s1)]:
            res[0] += 1
        if answers[i] == s2[i % len(s2)]:
            res[1] += 1
        if answers[i] == s3[i % len(s3)]:
            res[2] += 1
            
    if res[0] == max(res):
        ans.append(1)
    if res[1] == max(res):
        ans.append(2)
    if res[2] == max(res):
        ans.append(3)
        
    return ans
                