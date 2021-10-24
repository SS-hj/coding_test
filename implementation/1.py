N= int(input())
k = input().split()
row=1   # row 축 좌표

for j in range(len(k)):
    if k[j]=='R':
        if row<N+1:
            row+=1
    elif k[j]=='L':
        if row!=1:
            row-=1
col=1   # col 축 좌표
for j in range(len(k)):
    if k[j]=='D':
        if col<N+1:
            col+=1
    elif k[j]=='U':
        if col!=1:
            col-=1

print(col,row)