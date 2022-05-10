import sys
input=sys.stdin.readline

n = int(input()) # n개의 시험장
a = list(map(int,input().split())) # i 번 시험장의 응시자 수
# 총감독관이 감시가능한 응시자수, 부감독관이 감시가능한 응시자 수
b, c = map(int,input().split()) 
# 총감독관은 오직 1명, 부감독관은 여러명 가능

# 각 시험장마다 응시생을 모두 감독하기 위해 필요한 감독관의 최소수?

m = max(a)
d = [0] * (m+1)
for k in range(b+1):
    d[k] = 1


i = b+1
while i < m+1:
    # 점화식
    k = i+c
    if k > m+1:
        k = len(d)+1
    d[i:k] = [d[i-1] + 1]  * c
    
    i += c
    
cnt = 0

for k in a:
    cnt += d[k]

print(cnt)