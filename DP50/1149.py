n = int(input())
array = []

r, g, b = map(int, input().split())
array.append((r, g, b))
for _ in range(1, n):
    r, g, b = map(int, input().split())
    pR, pG, pB = array[-1]
    # 이전의 가능한 값들 중 최소값과 현재 값을 합쳐 저장
    R = r + min(pG, pB) 
    G = g + min(pB, pR)
    B = b + min(pR, pG)
    # 최종 들어가는 값은 각각의 RGB값이 아닌 현재 색이 _ 일 때의 누적값이 됨
    array.append((R,G,B))
print(min(array[-1]))