from collections import defaultdict

def solution(tickets):
    graph = defaultdict(list)
    
    for a, b in sorted(tickets, reverse=True):
        graph[a].append(b)
        
    res = []
    
    def dfs(a):
        while graph[a]:
            dfs(graph[a].pop())
        res.append(a)
        
    dfs('ICN')
    return res[::-1]