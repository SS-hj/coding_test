def solution(n):
    a,b=1,1
    for _ in range(n):a,b=b,a+b
    return a%1000000007