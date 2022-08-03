from itertools import permutations

def solution(k, dungeons):
    N = len(dungeons)
    plays = list(permutations(dungeons,N))
    ans = 0
    for play in plays:
        cnt = 0; power = k
        for j in range(N):
            if power >= play[j][0]:
                power-=play[j][1]
                cnt+=1
        ans = max(ans,cnt)
    return ans