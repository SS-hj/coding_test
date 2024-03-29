from collections import deque
import sys
input = sys.stdin.readline
n,m,k = map(int,input().split())
S2D2 = [list(map(int,input().split())) for _ in range(n)]
arr = [[5]*n for _ in range(n)]
trees = [[deque() for _ in range(n)] for _ in range(n)]
dr = [-1,-1,-1,0,0,1,1,1]
dc = [-1,0,1,-1,1,-1,0,1]
cnt = 0

for _ in range(m):
    x,y,z = map(int,input().split())
    trees[x-1][y-1].append(z)
    cnt += 1

while k>0:
    baby_trees = []
    for r in range(n):
        for c in range(n):
            # 봄: 나이가 어린 나무부터 자신의 나이만큼 양분을 먹고, 나이가 1 증가
            # 땅에 양분이 부족해 양분을 먹을 수 없으면 즉시 죽는다
            temp = deque()
            while trees[r][c] and arr[r][c]>=trees[r][c][0]:
                arr[r][c] -= trees[r][c][0]    # 양분먹기
                age = trees[r][c].popleft()+1
                temp.append(age)
                # 가을: 나무는 나이가 5의 배수이면, 인접한 8개의 칸에 나이가 1인 나무 추가 (범위 내에)
                if age%5==0:
                    for i in range(8):
                        nr, nc = r+dr[i], c+dc[i]
                        if 0<=nr<n and 0<=nc<n:
                            baby_trees.append((nr,nc))
                            cnt += 1
            # 여름: 죽은 나무 나이//2 만큼 해당 칸에 양분 추가
            while trees[r][c]:
                cnt -= 1
                arr[r][c] += trees[r][c].popleft()//2
            trees[r][c] = temp
            # 겨울: S2D2가 땅을 돌아다니면서 땅에 양분을 추가
            arr[r][c] += S2D2[r][c]
    for r,c in baby_trees:
        trees[r][c].appendleft(1)
    k -= 1
    
print(cnt)