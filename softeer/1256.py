H, K, R = map(int,input().split())
T = 2**H
tree = [[] for _ in range(T*2)]
for i in range(T,T*2):
    tree[i] = list(map(int,input().split()))

while R>0:
    height = 2
    check = H-1
    if tree[1]:
       tree[0].append(tree[1].pop(0)) 
    while height<T*2:
        if tree[height]:
            if check%2==0:    # 짝수면 오 => 왼
                for i in range(height*2-1, height-1,-1):
                    tree[i//2].append(tree[i].pop(0))
            else:               # 홀수면 왼 => 오
                for i in range(height, height*2):
                    tree[i//2].append(tree[i].pop(0))
        check -= 1
        height *= 2
    R -= 1
    
print(sum(tree[0]))