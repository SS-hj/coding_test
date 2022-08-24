def solution(n,a,b):
    cnt = 0
    while a != b: # 같은 부모가 되면 break
        cnt += 1
        a, b = (a+1)//2, (b+1)//2 # 부모로 갈때마다 += 1
    return cnt