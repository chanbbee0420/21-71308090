def solution(n):
    answer = 0
    for i in range(1, n+1):
        res = 0
        for j in range(i, n+1):
            res += j
            if res == n:
                answer += 1
            elif res > n:
                break
    
    return answer


# def expressions(num):
#     return len([i  for i in range(1,num+1,2) if num % i is 0])