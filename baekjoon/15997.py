arr = input().split()
point = dict(zip(arr,[0.]*4))
res = dict(zip(arr,[0.]*4))
gameList = []
    
def game(n, p): # n은 해당 게임 회차, p는 해당 게임이 진행될 확률을 의미
    if n==6:    # 6회차 게임이 끝난 경우 종료
        # 종료 점수 계산 (높은 점수 순으로 정렬)
        resRank = sorted(point.items(), key=lambda x: -x[1])
        # 4개의 나라가 승점이 같을 때
        if resRank[0][1] == resRank[1][1] == resRank[2][1] == resRank[3][1]:
            res[resRank[0][0]] += p/2   # 해당 게임이 진행될 확률 p * 4개 나라 중 2개 나라 뽑을 확률 2/4
            res[resRank[1][0]] += p/2
            res[resRank[2][0]] += p/2
            res[resRank[3][0]] += p/2
        # 1위 == 2위 == 3위 > 4위일 때
        elif resRank[0][1] == resRank[1][1] == resRank[2][1] > resRank[3][1]:
            res[resRank[0][0]] += p * (2/3)
            res[resRank[1][0]] += p * (2/3)
            res[resRank[2][0]] += p * (2/3)
        # 1위 > 2위 == 3위 == 4위
        elif resRank[0][1] > resRank[1][1] == resRank[2][1] == resRank[3][1]:
            res[resRank[0][0]] += p
            res[resRank[1][0]] += p * (1/3)
            res[resRank[2][0]] += p * (1/3)
            res[resRank[3][0]] += p * (1/3)
        # 1위 > 2위 == 3위 > 4위일 때
        elif resRank[0][1] > resRank[1][1] == resRank[2][1] > resRank[3][1]:
            res[resRank[0][0]] += p
            res[resRank[1][0]] += p * (1/2)
            res[resRank[2][0]] += p * (1/2)
        else:
            res[resRank[0][0]] += p
            res[resRank[1][0]] += p
        return
        
    else:
        A, B, W, D, L = gameList[n]
        if W:
            point[A] += 3
            game(n+1, p*W)
            point[A] -= 3
        if D:
            point[A] += 1
            point[B] += 1
            game(n+1, p*D)
            point[A] -= 1
            point[B] -= 1
        if L:
            point[B] += 3
            game(n+1, p*L)
            point[B] -= 3

for i in range(6):
    A, B, W, D, L = input().split()
    gameList.append([A, B, float(W), float(D), float(L)])
    
game(0, 1)

for i in res:
    print(res[i])