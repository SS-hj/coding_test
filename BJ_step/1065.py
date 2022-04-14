n = int(input())
# 1<x<=n의 각 자리가 등차수열을 이루는 경우의 수
# 두자리수까지는 전부 등차수열에 해당

cnt = 0
for x in range(1,n+1):
    if x < 100:
        cnt += 1
    else:
        d = int(str(x)[0]) - int(str(x)[1])
        for i in range(1,len(str(x))):
            if int(str(x)[i-1]) - int(str(x)[i]) != d:
                e = False
                break
            else:
                e = True
        if e == True:
            cnt += 1

print(cnt)