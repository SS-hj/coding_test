def solution(picks, minerals):
    check = []
    n = sum(picks)
    for i, mineral in enumerate(minerals):
        if i//5>=n:         # 더 사용할 곡괭이가 없을 때까지
            break
        if i%5==0:
            if i>0:
                check.append(temp)
            temp = [0,0,0]  # 다이아, 철, 돌
        if mineral=="diamond":
            temp[0]+=1
        elif mineral=="iron":
            temp[1]+=1
        else:
            temp[2]+=1
    if sum(temp):
        check.append(temp)
    check.sort(reverse=True)
    res = 0
    d = {0:[1,1,1], 1:[5,1,1], 2:[25,5,1]}
    idx = 0
    while check and idx<3:
        if picks[idx]>0:
            a,b,c = check.pop(0)
            res += a*d[idx][0]
            res += b*d[idx][1]
            res += c*d[idx][2]
            picks[idx] -= 1
        else:
            idx += 1
    
    return res