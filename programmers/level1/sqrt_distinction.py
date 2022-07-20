def solution(n):
    num = n ** 0.5
    if num == int(num):
        return (num + 1) ** 2
    else:
        return -1


def nextSqure(n):
    sqrt = n ** (1/2)

    if sqrt % 1 == 0:
        return (sqrt + 1) ** 2
    return -1