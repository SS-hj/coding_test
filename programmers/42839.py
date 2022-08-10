from itertools import permutations
def solution(nums):
    check = []; cnt = 0
    for i in range(1,len(list(nums))+1):
        check += list(map(''.join,permutations(list(nums),i)))
    check = list(set(map(int,check)))
    for c in check:
        if c < 2 : continue
        for i in range(2,c):
            if c%i==0:
                break
        else: cnt += 1
    return cnt