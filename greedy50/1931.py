n = int(input())
time=[]
ftime=[]
for i in range(n):
    t = list(map(int,input().split()))
    time += [t]
# 종료시간을 기준으로 정렬 후, 같은 종료시간일 경우 시작 시간 기준으로 정렬
time.sort(key=lambda x: (x[1], x[0]))

temp = time[0][1]
count = 1 # ftime이 제일 작은 회의는 자동으로 카운트 되고 시작
# ftime이 작은 것부터 해당 인덱스의 시작 시간 확인 -> 이전 ftime과 겹치지 않으면 해당 회의시간 카운트
for i in range(1,n):
    stime = time[i][0]
    if temp <= stime:
        count += 1
        temp = time[i][1]

print(count)