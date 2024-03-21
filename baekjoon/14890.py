n, l = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]

def check(A):
    visited = [False]*n
    for i in range(1,n):
        if A[i]!=A[i-1]:
            if A[i-1]+1==A[i] and i>=l:
                for k in range(l):
                    if A[i-1]!=A[i-1-k] or visited[i-1-k]:
                        return 0
                    visited[i-1-k]=True
            elif A[i-1]==A[i]+1 and n-i>=l:
                for k in range(l):
                    if A[i]!=A[i+k] or visited[i+k]:
                        return 0
                    visited[i+k]=True
            else:
                return 0
    return 1

cnt = 0
for r in range(n):
    cnt += check(arr[r])+check([arr[c][r] for c in range(n)])

print(cnt)