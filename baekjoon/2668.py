n = int(input())
adj = [[] for _ in range(n+1)]
for i in range(1, n+1):
    adj[int(input())].append(i)

def dfs(node, visited):
    visited.add(node)
    for next in adj[node]:
        if next not in visited and next not in res:
            dfs(next, visited)
        else:
            res.update(visited)
    visited.remove(node)
 
res = set()
for i in range(1,n+1):
    dfs(i, set())

print(len(res))
for r in sorted(res):
    print(r)