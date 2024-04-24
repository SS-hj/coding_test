n = int(input())
pu, nu = 0, 1
for _ in range(2, abs(n)+1):
    nu, pu = (nu + pu)%1000000000, nu
if n % 2 == 0 and n < 0:
    print(-1)
elif n == 0:
    print(0)
    nu = 0
else:
    print(1)
print(nu)