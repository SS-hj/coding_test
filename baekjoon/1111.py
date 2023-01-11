n = int(input())
arr = list(map(int,input().split()))
res = ["B"]

if len(arr)==1:
    print("A")
else:
    def check(idx, a, b):
        if idx == n-2 and arr[idx]*a+b == arr[idx+1]:
            res.append(arr[-1]*a+b)
        elif arr[idx]*a+b == arr[idx+1]:
            check(idx+1, a, b)
        return
            
    for a in range(-1000,1001):
        check(0, a, arr[1] - (arr[0]*a))
            
    if len(set(res)) > 2:
        print("A")
    else:
        print(res[-1])