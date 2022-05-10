from itertools import combinations #조합 함수

N = int(input())
S = [list(map(int, input().split())) for _ in range(N)]
members = [i for i in range(N)]
possible_team = []

# 조합으로 가능한 팀 생성해주기
for team in list(combinations(members, N//2)):
    possible_team.append(team)

print(possible_team)
min_stat_gap = 10000 # 갭이 가장 작은 값을 찾기 위하여
for i in range(len(possible_team)//2):
    # A 팀
    team = possible_team[i]
    stat_A = 0 # A팀 능력치
    for j in range(N//2):
        member = team[j] # 멤버
        for k in team:
            stat_A += S[member][k] # 멤버와 함께할 경우의 능력치들
            
    # A를 제외한 나머지 팀 (양쪽 끝에 있는 자리순으로 서로 여집합)
    team = possible_team[-i-1]
    stat_B = 0
    for j in range(N//2):
        member = team[j]
        for k in team:
            stat_B += S[member][k]
            
    min_stat_gap = min(min_stat_gap, abs(stat_A - stat_B))
    
print(min_stat_gap)