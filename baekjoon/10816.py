from collections import Counter
_ = input()
d = Counter(map(int,input().split()))
_ = input()
arr = list(map(int,input().split()))

for a in arr:
    if a in d:
        print(d[a], end=" ")
    else:
        print(0, end=" ")