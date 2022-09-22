from collections import defaultdict
def solution(tickets):
    answer = []; graph = defaultdict(list)
    for a,b in tickets:
        graph[a].append(b)
    for a, b in graph.items():
        graph[a].sort()
    def dfs(s):
        while graph[s]:
            dfs(graph[s].pop(0))
        if not graph[s]:
            answer.append(s)
    dfs("ICN")
    return answer[::-1]