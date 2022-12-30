def solution(n, costs):
    res = 0
    parent = [i for i in range(n)]
    def find_parent(x):
        return x if parent[x]==x else find_parent(parent[x])
    def union(a,b):
        a, b = find_parent(a),find_parent(b)
        if a < b:
            parent[b] = a
        else:
            parent[a] = b
    costs.sort(key = lambda x : x[2])
    for edge in costs:
        a, b, cost = edge
        if find_parent(a) != find_parent(b):
            union(a, b)
            res += cost
    return res