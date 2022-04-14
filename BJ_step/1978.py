import sys
input=sys.stdin.readline

n = int(input())
arr = list(map(int,input().split()))

cnt = 0
for k in arr:
    e = True
    if k == 1:
        continue
    if k <= 2:
        cnt += 1
    else:
        for i in range(2,k):
            if k % i == 0:
                e = False
            else:
                continue
        if e == True:
            cnt += 1
        
print(cnt)