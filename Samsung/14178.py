T = int(input())

for t in range(1, T + 1):
    N,D=map(int,input().split())
    cnt = 0
    while N > 0:
        N -= 2*D+1
        cnt += 1
    print('#'+str(t), cnt)