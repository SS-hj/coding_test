while True:
    n = int(input())
    if n == 0:
        break
    if n == 1:
        print(1)
    else:
        p = [1]*(2*n+1)
        p[0] = 0
        p[1] = 0              
        for a in range(2*n+1):
            if p[a]: # True 이면 (소수 아니라고 처리가 안 되었으면)
                for b in range(a*2, 2*n+1, a):
                    p[b]=0  # 소수가 아니면 False
        print(sum(p[n+1:2*n+1]))