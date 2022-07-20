def solution(arr, divisor): 
	return sorted([n for n in arr if n%divisor == 0]) or [-1]



# def solution(arr, divisor):
#     res = []
#     for i in range(len(arr)):
#         if arr[i] % divisor == 0:
#             res.append(arr[i])

#     res.sort()

#     if len(res) >= 1:
#         return res
#     else:
#         return [-1]