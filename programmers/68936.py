def solution(arr):
    cnt = [0, 0]
    def check(sr,sc,l):
        num = sum(sum(A[sc:sc+l]) for A in arr[sr:sr+l])
        if  num == l**2:
            cnt[1] += 1
        elif num == 0:
            cnt[0] += 1
        else:
            check(sr,sc,l//2)
            check(sr+l//2,sc,l//2)
            check(sr,sc+l//2,l//2)
            check(sr+l//2,sc+l//2,l//2)
    check(0,0,len(arr))
    return cnt