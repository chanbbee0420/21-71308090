def solution(brown, yellow):
    size = brown + yellow
    for width in range(1, size + 1):
        if size / width == int(size / width):
            length = size / width
            if length >= width:
                if 2*length + 2*width - 4 == brown:
                    return [length, width]


# def solution(brown, red):
#     for i in range(1, int(red**(1/2))+1):
#         if red % i == 0:
#             if 2*(i + red//i) == brown-4:
#                 return [red//i+2, i+2]