def solution(begin, target, words):
    n = len(words)
    visited = [False]*n
    res = []
    def check(present, nextt):
        cnt = 0
        for p, n in zip(present,nextt):
            if p!=n:
                cnt += 1
            if cnt > 1:
                return False
        return True

    def change(x, cnt):
        if words[x] == target:
            res.append(cnt)
            return
        visited[x] = True
        for i in range(n):
            if not visited[i] and check(words[x], words[i]):
                change(i, cnt+1)

    for i in range(n):
        if check(begin, words[i]):
            change(i, 1)
    return min(res) if res else 0