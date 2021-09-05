n, m = map(int,input().split())

res = 0
for i in range(n):
    k = list(map(int,input().split()))
    # 현재 입력한 행에서 최소값 저장
    min_val = min(k)
    # 최소값들 중 최대값을 저장
    res = max(res, min_val)
    
print(res)
