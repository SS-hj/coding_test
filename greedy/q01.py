n = int(input())

arr = list(map(int,input().split()))
arr.sort(reverse=True)
visited = [1] * n  # 0이면 처리된 것

i = 0
cnt = 0 
while i < n:
    temp = [arr[i]*visited[i] for i in range(n)]
    num = temp.count(arr[i])
    if num >= arr[i] > 0 :
        for k in range(i,num):
            visited[k] = 0
        cnt += 1
    i += num
print(cnt)