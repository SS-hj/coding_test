from collections import Counter

n = int(input())
word = input()
a = Counter(word)
al = len(word)
res = 0

for _ in range(n-1):
    word = input()
    b = Counter(word)
    bl = len(word)
    temp = 0
    for s in a:
        temp += abs(a[s]-b[s]) if s in b else a[s]
        del b[s]
    for s in b:
        temp += b[s]
    if temp<2 or (temp==2 and al==bl):
        res += 1

print(res)