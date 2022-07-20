# def solution(a, b):
#     res = 0
#     days = ['FRI','SAT','SUN','MON','TUE','WED','THU']
#     months = [31, 29 ,31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

#     for i in range(a-1):
#         res += months[i]
        
#     res += b - 1 
#     answer = res % 7
#     return days[answer]

def solution(a, b):

    months = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    days = ['FRI', 'SAT', 'SUN', 'MON', 'TUE', 'WED', 'THU']
    return days[(sum(months[:a-1])+b-1)%7]