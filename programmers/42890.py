from itertools import combinations
def solution(relation):
    visited = set()
    arr = [list(x) for x in zip(*relation)] # 전치 행렬 구하기
    n, m = len(arr), len(arr[0])
    for i in range(n):
        for combs in combinations(range(n),i+1):
            for v in visited:
                # 최소성 만족 못하면 계산 안함
                if set(v).issubset(set(combs)): # issubset : 집합 포함관계 확인
                    break
            else:
                temp = ["".join(arr[comb][j] for comb in combs) for j in range(m)]
                # 유일성 만족하면 추가
                if len(set(temp))==m:
                    visited.add(combs)
    return len(visited)