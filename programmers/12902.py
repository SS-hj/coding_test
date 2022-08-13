def solution(n):
    if n % 2: return 0
    a = b = 1
    for _ in range(n//2):
        a, b = b, (4*b - a) % 1000000007
    return b