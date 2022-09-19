T = int(input())
# 다리끼리는 서로 겹쳐질 수 없다고 할 때 다리를 지을 수 있는 경우의 수

def check(n, m):
    i = 0
    cnt = 1
    for i in range(1,n+1):
        num = n - i 
        cnt *= m - i + 1 - num
    return cnt

for t in range(T):
    n, m = map(int,input().split())
    print(check(n, m))