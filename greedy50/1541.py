s = list(input().split('-')) # 첫번째 값 제외하고 이 s 리스트를 기준으로 빼주기

temp = []
sum = 0
for i in s:
    temp += [i.split('+')]

for j in range(len(temp)):
    if j==0:
        for k in temp[j]:
            sum += int(k)
    else:
        for k in temp[j]:
            sum -= int(k)
        
print(sum)