T = int(input())
for _ in range(T):
    sx,sy,ex,ey = map(int,input().split())
    n = input()
    check = [map(int,input().split()) for _ in range(int(n))]
    cnt = 0
    for a,b,r in check:
        sd, ed = ((a-sx)**2+(b-sy)**2)**0.5, ((a-ex)**2+(b-ey)**2)**0.5
        if (sd < r and ed > r) or (ed < r and sd > r):
            cnt += 1
    print(cnt)