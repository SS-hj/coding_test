n, k = map(int,input().split())

res = 0
j = n%k # 1을 더하는 개수
n -= j

while n > 0:
    n = n//k
    res+=1 # k를 나누는 개수
res = res+j-1

print(res)