def solution(N):
    cnt = 0
    while N > 0:
        if N % 2:
            cnt += 1
        N //= 2
    return cnt



# def solution(n):
#     return bin(n).count('1')