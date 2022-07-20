from collections import deque

def solution(prices):
    queue = deque(prices)
    res = []
    
    while queue:
        price = queue.popleft()
        t = 0
        for i in queue:
            t += 1
            if price > i:
                break
        res.append(t)
    return res