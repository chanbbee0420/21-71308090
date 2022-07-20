def solution(num):
    res = 0
    if num == 1:
        return 0
    
    while True:
        num = num/2 if not num % 2 else num*3+1
        res += 1
        if num == 1:
            return res
        elif res == 500:
            return -1
        
    return res


def collatz(num):
    for i in range(500):
        num = num / 2 if num % 2 == 0 else num*3 + 1
        if num == 1:
            return i + 1
    return -1