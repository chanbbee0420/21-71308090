def solution(n):
    ls = list(str(n))
    ls.sort(reverse = True)
    return int("".join(ls))

	
# def solution(n):
#     res = ''
#     arr = sorted([i for i in str(n)], reverse=True)
#     for dig in arr:
#         res += dig
        
    
#     return int(res)