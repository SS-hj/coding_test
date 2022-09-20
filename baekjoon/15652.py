from itertools import combinations_with_replacement # 중복조합
N, K = map(int,input().split())
for comb in list(combinations_with_replacement(range(1,N+1),K)):
    print(*comb)