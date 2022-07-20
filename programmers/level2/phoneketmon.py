def solution(nums):
    length = len(nums) // 2
    cnt = 0
    tmp = list(set(nums))
    
    for i in tmp:
        if (cnt < length):
            cnt += 1
            
    return cnt

# def solution(ls):
#     return min(len(ls)/2, len(set(ls)))
	