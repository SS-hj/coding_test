n = int(input())
d_len = list(map(int,input().split()))
price = list(map(int,input().split()))


# 마지막은 상관 x
price.pop(-1)

# 현재 값보다 작은 값(최소가 아니더라도)이 나오기 전까지 현재값 * 작은거 나오는 섬까지의 거리
sum = 0
i = 0
while True:
    # 현재값 i 보다 다음에 나오는 작은 값이 있는지 있다면 인덱스 저장
    idx = i
    for k in range(i,n-1):
        if price[k] < price[idx]:
            idx = k
            break
        else: continue
    # idx 직전까지 현재값의 직전까지들의 거리 합계
    dd = 0
    if idx == i: # 만약 현재값이 최소값이면
        for j in range(i,n-1):
            dd += d_len[j]
        sum += price[i] * dd
        break
    else:
        for j in range(i,k):
            dd += d_len[j]
        sum += price[i] * dd
    i = k
print(sum)
