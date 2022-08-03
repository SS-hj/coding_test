def solution(n, wires):
    def find(a):
        return a if uf[a] < 0 else find(uf[a])
    def merge(a, b):
        pa = find(a)
        pb = find(b)
        if pa == pb: return # 부모가 같으면 이미 merge된 것
        uf[pa] += uf[pb] # 누가 더 상위 부모다 개념 X
        uf[pb] = pa # 둘 중 아무거나에 얘가 pa 자식으로 처리됐다고 표시
        
    answer = int(1e9)
    k = len(wires)
    for i in range(k):
        uf = [-1 for _ in range(n+1)]
        tmp = [wires[x] for x in range(k) if x != i] # i번쨰를 제외한 wires들
        for a, b in tmp: merge(a, b)
        v = [x for x in uf[1:] if x < 0]
        answer = min(answer, abs(v[0]-v[1]))
    return answer