from collections import defaultdict
def solution(n, results):
    win, lose = defaultdict(set), defaultdict(set)
    cnt = 0
    for u,v in results:
        win[u].add(v)
        lose[v].add(u)
    for i in range(1,n+1):
        for winner in win[i]: lose[winner].update(lose[i])
        for loser in lose[i]: win[loser].update(win[i])
    for i in range(n+1):
        if len(win[i]) + len(lose[i]) == n-1: cnt += 1
    return cnt