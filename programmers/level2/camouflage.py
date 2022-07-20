def solution(clothes):
    dic = {}
    res = 1
    
    for c, category in clothes:
        dic[category] = dic.get(category, 0) + 1
        
    for category in dic:
        res *= (dic[category]) + 1
    
    return res - 1


# def solution(clothes):
#     from collections import Counter
#     from functools import reduce
#     cnt = Counter([kind for name, kind in clothes])
#     answer = reduce(lambda x, y: x*(y+1), cnt.values(), 1) - 1
#     return answer