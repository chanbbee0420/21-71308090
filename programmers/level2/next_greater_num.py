def solution(n):
    c = bin(n).count('1')
    for m in range(n+1,1000001):
        if bin(m).count('1') == c:
            return m

def nextBigNumber(n):
    num1 = bin(n).count('1')
    while True:
        n += 1
        if num1 == bin(n).count('1'):
            break
    return n