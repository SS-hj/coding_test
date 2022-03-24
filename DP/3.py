n = int(input())
k = list(map(int,input().split()))

# DP 테이블 초기화
d = [0] * 100

# 보텀업
d[0] = k[0]
d[1] = max(k[0], k[1])
for i in range(2, n):
    d[i] = max(d[i-1], d[i-2] + k[i])
    
print(d[n-1])