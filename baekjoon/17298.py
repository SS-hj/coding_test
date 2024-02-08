n = int(input())
arr = list(map(int,input().split()))
stack = [0]
res = [-1]*n

for i in range(1,n):
    while stack and arr[stack[-1]]<arr[i]:
        res[stack.pop()]=arr[i]
    stack.append(i)
    
print(*res)