t = int(input())

# 300s 60s 10s
k, r = divmod(t, 300)
m5 = k
k, r = divmod(r, 60)
m1 = k
k, r = divmod(r, 10)
s10 = k
if r == 0:
    print(m5, m1, s10)
else:
    print(-1)