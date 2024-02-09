h,w = map(int,input().split())
arr = [0]+list(map(int,input().split())) + [0]

prefix = [0 for _ in range(w+2)]
suffix = [0 for _ in range(w+2)]

for i in range(1,w+1):
  prefix[i] = max(prefix[i-1],arr[i])
for i in range(w,0,-1):
  suffix[i] = max(suffix[i+1],arr[i])

cnt = sum(min(suffix[i],prefix[i]) for i in range(1,w+1))
print(cnt - sum(arr))