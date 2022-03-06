n = int(input())
array = []
for i in range(n):
    array += [int(input())]
    
array.sort(reverse=True)

for j in array:
    print(j, end=' ')