m = int(input())
n = int(input())
# m <= x <= n 의 소수 x들의 합과 최솟값 출력

arr = []
for x in range(m,n+1):
    e = True
    if x == 1:
        continue
    if x <= 2:
        arr += [x]
    else:
        for i in range(2,x):
            if x % i == 0:
                e = False
            else:
                continue
        if e == True: # 소수이면
            arr += [x]
            
if len(arr)==0:
    print(-1)
else:
    print(sum(arr))
    print(arr[0])