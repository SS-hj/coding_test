n, m = map(int,input().split())
x, y, d = map(int,input().split())
l=[]
for i in range(n):
    l.append(list(map(int,input().split())))
# l: 실제 지도는
# map: 방문한 위치 표시용 지도
map=[[0]*m for _ in range(n)]
# 시작 위치 map에 표시
map[x][y]=1
# 0-상(북) 1-우(동) 2-하(남) 3-좌(서)
def turn_left(d):
    if d==0:
        return 3
    else:
        return d-1
# 한 칸 이동 가능한 움직임들
go=[(-1,0),(0,1),(1,0),(0,-1)]

cnt=1
turn_time=0
while True:
    d=turn_left(d)
    # 안 가본 곳이면서 육지인 경우 한칸 전진
    if map[x+go[d][0]][y+go[d][1]]==0 and l[x+go[d][0]][y+go[d][1]]==0: 
        x+=go[d][0]
        y+=go[d][1]
        map[x][y]=1
        cnt+=1
        turn_time=0
        continue
    else:
        turn_time+=1
    if turn_time==4:
        back_d=turn_left(turn_left(d))
        # 네 방향 모두 갔었지만, 뒷칸이 육지인 경우 경우 한칸 후퇴
        if l[x+go[back_d][0]][y+go[back_d][1]]==0:
            x+=go[back_d][0]
            y+=go[back_d][1]
            # 이미 이동했던 칸이므로 count하지 않음
        else: # 뒷칸이 바다인 경우 game over
            break
        turn_time=0
print(cnt)