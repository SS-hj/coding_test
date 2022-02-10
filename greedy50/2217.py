n = int(input())
rope  = []
for i in range(n):
    rope += [int(input())]

rope.sort()

res = []
for i in range(n):
    res += [rope[i] * (n-i)]

print(max(res))