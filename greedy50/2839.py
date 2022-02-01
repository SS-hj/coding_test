n = int(input())

# 일단 5로 나누기
k,r = divmod(n,5)

if r==0:
    print(k)
else:
    # r이 3으로 나누어떨어지지 않는 경우 5를 다시 더하고 3으로 나눠보기
    while r<=n:
        d,o=divmod(r,3)
        if o==0:
            print(k+d)
            break
        else:
            k-=1
            r+=5

# 3으로만 나누어도 떨어지지 않는다면 -1 출력
if r>n:
    print(-1)
