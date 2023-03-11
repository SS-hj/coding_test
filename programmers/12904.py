def solution(s):
    n = len(s)
    maxCnt = 0
    for i in range(n):
        for j in range(i+1,n+1):
            temp = s[i:j]
            if temp == temp[::-1] and maxCnt < j-i:
                maxCnt = j-i
    return maxCnt