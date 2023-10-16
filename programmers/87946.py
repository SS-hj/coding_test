from itertools import permutations
def solution(k, dungeons):
    totalRes = 0
    for p in permutations(dungeons):
        power = k
        res = 0
        for a, b in p:
            if a > power:
                break
            power -= b
            res += 1
        totalRes = max(totalRes, res)
    return totalRes