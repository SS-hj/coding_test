T = int(input())
array = []

for k in range(T):
    array += [int(input())]

# 0 에 대한 배열 & 1에 대한 배열
d = [[0] * 41 for _ in range(2)]

d[0][0] = d[1][1] = 1  # 피보나치 0 일 때 0 리턴 o, 1일 때 1 리턴 o
d[0][1] = d[1][0] = 0  # 피보나치 0 일 때 1 리턴 x, 1일 때 0 리턴 x

# 피보나치 함수를 반복문으로 구현 (보텀업 다이나믹 프로그래밍)
for i in range(2, 41):
    # 원래 피보나치의 점화식
    # f(n) = f(n-1) + f(n-2)
    d[0][i] = d[0][i-1]+d[0][i-2]
    d[1][i] = d[1][i-1]+d[1][i-2]

for n in array:
    print(d[0][n], d[1][n])