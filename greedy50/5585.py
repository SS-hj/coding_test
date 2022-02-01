n = int(input())

r = 1000-n
cnt = 0

m = [500,100,50,10,5]
for i in m:
    k, r = divmod(r, i)
    cnt += k
cnt += r

print(cnt)