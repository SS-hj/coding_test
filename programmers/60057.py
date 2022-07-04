def solution(s):
    answer = 9999
    length = len(s)
    for i in range(1,length//2+1):
        idx = list(range(0,length+1,i))
        temp = [s[idx[0]:idx[1]]]
        cnt = 1
        for k in range(2,len(idx)):
            if temp[-1] == s[idx[k-1]:idx[k]]:
                cnt += 1
            else:
                if cnt == 1:
                    temp.append(s[idx[k-1]:idx[k]])
                else:
                    temp.append(cnt)
                    temp.append(s[idx[k-1]:idx[k]])
                cnt = 1
        if cnt > 1:
            temp.append(cnt)
        if idx[-1] < len(s):
            temp.append(s[idx[-1]:])
        answer = min(answer, len("".join(map(str, temp))))
    return answer