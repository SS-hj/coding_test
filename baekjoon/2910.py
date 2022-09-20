from collections import Counter
input()
arr = Counter(map(int,input().split())).most_common()
for a in arr:
    temp = [a[0]]*a[1]
    print(*temp, end=' ')