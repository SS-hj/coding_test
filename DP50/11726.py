n = int(input())
cnt = 1
if n <= 3:
    print(n)
else:
    d = [0]*n
    d[0] = 1
    d[1] = 2
    for i in range(2,n):
        d[i] = d[i-1]+d[i-2]
    print(d[n-1]%10007)