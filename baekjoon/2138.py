n = int(input())
arr = list(map(int,input()))
target = list(map(int,input()))
        
def check():
    temp = arr[:]
    cnt = 0
    for i in range(1, n):
        if temp[i-1] == target[i-1]:
            continue
        cnt += 1
        temp[i-1] = 1 - temp[i-1]
        temp[i] = 1 - temp[i]
        if i+1<n:
            temp[i+1] = 1 - temp[i+1]
    return cnt if temp==target else 1e9

res = check()
arr[0] = 1 - arr[0]
arr[1] = 1 - arr[1]
res = min(res, check()+1)

print(res if res!=1e9 else -1)