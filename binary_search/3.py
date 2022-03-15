n, m = map(int,input().split())
n_list = list(map(int,input().split()))

start = 0
end = max(n_list)

res = 0
while(start<=end):
    total = 0
    mid = (start + end) // 2
    for x in n_list:
        # 자른 떡의 양 계산
        if x > mid:
            total += x- mid
    # 떡의 양이 부족한 경우 (왼쪽 탐색)
    if total < m:
        end = mid - 1
    # 떡의 양이 충분한 경우 (오른쪽 탐색)
    else:
        res = mid
        start = mid + 1

print(res)