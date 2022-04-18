n, m = map(int,input().split())
graph = [input() for _ in range(n)]
cnt = []

for a in range(n-7):
    for b in range(m-7):
        index1 = 0 # 짝수면 W 홀수면 B로 바꾸는 경우에 대한 카운트
        index2 = 0 # 홀수면 W 짝수면 B로 바꾸는 경우에 대한 카운트
        for i in range(a, a+8):
            for j in range(b, b+8):
                if (i+j) % 2 == 0: # 짝수일 경우 
                    if graph[i][j] != 'W': 
                        index1 += 1
                    if graph[i][j] != 'B':
                        index2 += 1
                else:
                    if graph[i][j] != 'B':
                        index1 += 1
                    if graph[i][j] != 'W':
                        index2 += 1
        cnt.append(min(index1, index2))

print(min(cnt))