n = int(input())
d = [0] * (n+1)

d[0] = 0
d[1] = 1

# 피보나치 함수를 반복문으로 구현 (보텀업 다이나믹 프로그래밍)
for i in range(2, n+1):
    # 원래 피보나치의 점화식
    # f(n) = f(n-1) + f(n-2)
    d[i] = d[i-1]+d[i-2]

print(d[n])