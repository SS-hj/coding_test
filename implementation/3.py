n=input()
row=int(n[1])
col=int(ord(n[0]))-int(ord('a'))+1

# 이동 가능한 step들을 정의한 리스트
steps=[(-2,-1),(-1,-2),(2,-1),(1,-2),(-2,1),(-1,2),(2,1),(1,2)]
cnt=0
for step in steps:
    next_row=row+step[0]
    next_col=col+step[1]
    # 문제의 제한사항 조건을 코드화
    if next_row>=1 and next_row<=8 and next_col>=1 and next_row<=8:
        cnt+=1
print(cnt)