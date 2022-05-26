def solution(a, v):
    def dfs(pos, cur):
        if pos == len(a):
            return (cur == 0)  # cur == 0 이면 1을 반환 아니면 0을 반환하므로 target값에 도달한 것들을 count 하는 것이 된다.
        return dfs(pos + 1, cur + a[pos]) + dfs(pos + 1, cur - a[pos])
    return dfs(0, v)