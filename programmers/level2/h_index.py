# def solution(citations):
#     citations.sort()
#     for idx, c in enumerate(citations):
#         if c >= len(citations) - idx:
#             return len(citations) - idx
#     return 0


def solution(citations):
    citations.sort(reverse=True)
    answer = max(map(min, enumerate(citations, start=1)))
    return answer

# 1) min(index,value) 부분은 가능할 수 있는 모든 h-index를 추출하는 부분 2) max(~) 값은 가능할 수 있는 모든 h-index 중 가장 큰 값을 추출하는 부분으로 생각하시면 됩니다. 예를들어 [6, 5, 4, 1, 0]의 경우에선 min~ 부분은 min(1, 6), min(2, 5), min(3, 4), min(4, 1), min(5, 0), 즉 해당 인용수 이상의 논문개수와 해당 논문의 인용수 중 더 작은 숫자를 고르는 작업을 하고(h-index로 가능한 숫자 추출), max~부분은 앞에서 골라진 (1, 2, 3, 1, 0) 중 가장 큰 숫자를 뽑아 실제 h-index를 구하는 방법입니다

# sort로 정렬해서 가장 큰값부터 작은값으로 정렬한후, enumerate로 (index, value)형태로 묶는다. 그리고 최댓값(start = 1)부터 각 value에 대해 최솟값 value의 값을 min으로 추출하고, 이 추출된 값은 enumerate가 끝나는 citations 리스트의 크기에 해당하는 갯수가 나온다. 이들을 map으로 묶으면, 한 value의 입장에서 보는 최솟값 value의 집합이 나온다. 즉 h값들의 집합이나온다. h값중 최대값을 max로 뽑아서 출력하면 된다.