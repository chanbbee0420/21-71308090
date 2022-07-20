def solution(n,a,b):
    cnt = 1
    
    while True:
        if ((a+1)//2) == ((b+1)//2):
            return cnt
            break
        else:
            a = (a+1)//2
            b = (b+1)//2
            cnt += 1