def water_melon(n):
    s = "수박" * n
    return s[:n]

def solution(n):
    T = '수박'
    res = ''
    if n % 2 == 0:
        res += T*(n//2)
    else:
        res += T*(n//2)+'수'
    return res