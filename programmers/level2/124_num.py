def solution(n):
    T = "124"
    q, r = divmod(n - 1, 3)
    if q == 0:
        return T[r]
    else:
        return solution(q) + T[r]


# n 진법
# import string

# tmp = string.digits+string.ascii_lowercase
# def convert(num, base) :
#     q, r = divmod(num, base)
#     if q == 0 :
#         return tmp[r] 
#     else :
#         return convert(q, base) + tmp[r]