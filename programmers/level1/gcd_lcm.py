def gcdlcm(a, b):
    c, d = max(a, b), min(a, b)
    t = 1
    while t > 0:
        t = c % d
        c, d = d, t
    answer = [c, int(a*b/c)]

    return answer



# def solution(n, m):
#     def gcd(n, m):
#         while m:
#             n, m = m, n % m

#         return n
    
#     def lcm(n, m):
#         return n * m / gcd(n, m)
    
#     return [gcd(n,m), lcm(n,m)]
