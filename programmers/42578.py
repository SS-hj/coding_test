import collections

def solution(clothes):
    cnt_set = collections.Counter(type for cloth, type in clothes).most_common()
    res = 1
    for k,v in cnt_set:
        res *= v + 1 # 해당 종류의 옷을 안 잆는 경우 +1을 해주어 전부 곱
    return res-1 # 아무 옷도 안 입는 경우를 제외 -1