n = int(input())
arr = list(range(1,n+1))
num = 1
idx = 0
while len(arr) > 1:
    print(arr, (idx+num**3)%len(arr)-1)
    idx = (idx+num**3)%len(arr)-1
    arr.pop(idx)
    num+=1
print(arr[0])