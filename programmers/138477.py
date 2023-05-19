def solution(k, score):
    temp, answer = [score[0]], [score[0]]
    for s in score[1:]:
        for i in range(len(temp)-1,-1,-1):
            if temp[i]>=s:
                temp = temp[:i+1]+[s]+temp[i+1:]
                break
            elif i==0:
                temp = [s]+temp
        if len(temp) > k:
            temp.pop()
        answer.append(temp[-1])
    return answer