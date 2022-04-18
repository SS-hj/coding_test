import sys
input=sys.stdin.readline

n = int(input())
data = [list(map(int, input().split())) for _ in range(n)]
rank = [] # 등수정보를 저장할 리스트

 
for i in range(n):
    cnt = 0
    for j in range(n):
        if data[i][0] < data[j][0] and data[i][1] < data[j][1]: # 몸무게와 키 모두 자신보다 큰 사람의 수를 카운트
            cnt += 1 
    rank.append(cnt + 1)  # 등수는 자신보다 몸무계 키 모두 큰 사람의 수 + 1
 
for d in rank:
    print(d,end=" ")
