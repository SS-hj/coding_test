def solution(a, b, n):
    cnt = 0
    while n>=a:
        cnt += b*(n//a)
        n = n%a + b*(n//a)
    return cnt