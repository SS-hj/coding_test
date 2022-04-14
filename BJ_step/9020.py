import sys
input=sys.stdin.readline

n = int(input())
arr = [int(input()) for _ in range(n)]

# 절반을 나누어서
# 오른쪽으로 왼쪽으로 => 둘 다 소수인 경우 이를 출력

for k in arr:
    p = [True]*(k+1)
    p[0]=False
    p[1]=False

    for a in range(len(p)):
        if p[a]: # True 이면 (소수 아니라고 처리가 안 되었으면)
            for b in range(a*2, k+1, a):
                p[b]=False  # 소수가 아니면 False
            
    l = list(range(1,k//2+1))
    r = list(range(k//2,k+1))
    for i in range(k//2+1):
        ln = l[-(i+1)]
        rn = r[i]
        if p[ln] == True & p[rn] == True:
            print(ln, rn)
            break