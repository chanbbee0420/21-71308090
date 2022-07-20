def sum_digit(number):
    if number < 10:
        return number
    return (number % 10) + sum_digit(number // 10) 


# def sum_digit(number):
#     return sum([int(i) for i in str(number)])



# def solution(n):
#     dig = [i for i in str(n)]
#     res = 0
#     for i in dig:
#         res += int(i)
        
#     return res


	