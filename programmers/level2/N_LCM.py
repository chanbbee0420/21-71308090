def solution(arr):
    def gcd(n, m):
        while m:
            n, m = m, n % m

        return n
    
    def lcm(n, m):
        return n * m / gcd(n, m)
    
    arr1 = sorted(arr)
    
    while len(arr1) > 1:
        a = arr1.pop()
        b = arr1.pop()
        arr1.append(lcm(a,b))
        
    return arr1[0] 




#2
# def solution(arr):
#     def gcd(n, m):
#         while m:
#             n, m = m, n % m
#         return n
    
#     res = arr[0]
#     for i in arr:
#         res = i * res / gcd(i, res)
        
#     return res




#3
# from fractions import gcd


# def nlcm(num):      
#     answer = num[0]
#     for n in num:
#         answer = n * answer / gcd(n, answer)

#     return answer