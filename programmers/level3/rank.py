from collections import defaultdict

def solution(n, results):
    answer = 0
    win_graph = defaultdict(set)    # 이긴 애들
    lose_graph = defaultdict(set)   # 진 애들
    
    for winner,loser in results:        # 결과에서 이기고 진 애들 그래프화
        win_graph[loser].add(winner)
        lose_graph[winner].add(loser)

    for i in range(1,n+1):         
        for winner in win_graph[i]:                    # i한테 진 애들은 i를 이긴 애들한테도 진 것
            lose_graph[winner].update(lose_graph[i])
        for loser in lose_graph[i]:                     # i한테 이긴 애들은 i한테 진 애들한테도 이긴 것
            win_graph[loser].update(win_graph[i])
    
    for i in range(1,n+1):
        if len(win_graph[i]) + len(lose_graph[i]) == n-1:   # i한테 이기고 진 애들 합쳐서 n-1이면 순위가 결정된 것
            answer += 1

    return answer


# NOT EFFICIENT
# def solution(n, results):
#     answer = 0
#     board = [[0]*n for _ in range(n)]
    
#     for a,b in results:
#         board[a-1][b-1] = 1
#         board[b-1][a-1] = -1
        
#     for k in range(n):
#         for i in range(n):
#             for j in range(n):
#                 if i == j or board[i][j] in [1,-1]:
#                     continue
#                 if board[i][k] == board[k][j] == 1:
#                     board[i][j] = 1
#                     board[j][i] = board[k][i] = board[j][k] = -1
#     for row in board:
#         if row.count(0) == 1:
#             answer += 1
#     return answer