def solution(A,B):
    lst1 = sorted(A)
    lst2 = sorted(B, reverse=True)  
    ans = 0
    
    for i in range(len(A)):
        ans += (lst1[i] * lst2[i])
        
    return ans


def getMinSum(A,B):
    return sum(a*b for a, b in zip(sorted(A), sorted(B, reverse = True)))