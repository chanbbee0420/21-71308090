def Harshad(n):
    return n % sum([int(c) for c in str(n)]) == 0

# def solution(x):
#     digs = list(str(x))
#     dig_sum = 0
#     for dig in digs:
#         dig_sum += int(dig)
        
#     return x % dig_sum == 0