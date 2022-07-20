# from heapq import heapify, heappush, heappop
# def solution(scoville, K):
#     heapify(scoville)
#     for i in range(1000000):
#         try:
#             heappush(scoville, heappop(scoville)+(heappop(scoville)*2))
#             if scoville[0] >= K: return i+1
#         except:
#             return -1







import heapq as hq

def solution(scoville, K):

    hq.heapify(scoville)
    answer = 0
    while True:
        first = hq.heappop(scoville)
        if first >= K:
            break
        if len(scoville) == 0:
            return -1
        second = hq.heappop(scoville)
        hq.heappush(scoville, first + second*2)
        answer += 1  

    return answer






import heapq

# def solution(scoville, k):
    
#     heap = []
#     for num in scoville:
#         heapq.heappush(heap, num)
        
#     mix_cnt = 0
#     while heap[0] < k:
#         try:
#             heapq.heappush(heap, heapq.heappop(heap) + (heapq.heappop(heap) * 2))
#         except IndexError:
#             return -1
#         mix_cnt += 1
#     return mix_cnt