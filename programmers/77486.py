def solution(enroll, referral, seller, amount):
    N = len(enroll); res = [0]*(N+1); d = {"center":0}; parent = [0]*(N+1)
    for i,v in enumerate(enroll):
        d[v] = i+1
    for i in range(N):
        if referral[i]!="-":
            parent[i+1] = d[referral[i]]
    def find_parent(x,price):
        r = price//10
        res[x] += price - r
        if parent[x] != x and r > 0 : find_parent(parent[x], r)
    for s,a in zip(seller,amount):
        find_parent(d[s],a*100)
    return res[1:]