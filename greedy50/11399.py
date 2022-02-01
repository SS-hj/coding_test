n = int(input())
k = list(map(int,input().split()))

k.sort() 
sum = 0
for i in range(len(k)):
    temp = k[0:i+1]
    for j in temp:
        sum += j

print(sum)