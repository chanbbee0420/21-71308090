def solution(s):
    s = s.split(' ')
    nums = [int(i) for i in s]
    nums.sort()
    return str(nums[0]) + " " + str(nums[-1])


# def solution(s):
#     s = list(map(int,s.split()))
#     return str(min(s)) + " " + str(max(s))

