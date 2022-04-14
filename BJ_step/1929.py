m, n = map(int,input().split())
# m <= x <= n 의 소수 x 찾기

p = [True]*(n+1)
p[0]=False
p[1]=False

for a in range(len(p)):
    if p[a]: # True 이면 (소수 아니라고 처리가 안 되었으면)
        # 1 2 3 => 2 4 6
        for b in range(a*2, n+1, a):
            p[b]=False  # 소수가 아니면 False

for k in range(m, len(p)):
    if p[k] == True:
        print(k)