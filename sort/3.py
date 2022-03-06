n = int(input())
array = []

for i in range(n):
    array += [list(input().split())]

array.sort(key=lambda x: (x[1]))

for i in range(n):
    print(array[i][0], end=' ')