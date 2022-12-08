from collections import Counter

def solution(topping):
    answer = 0
    dic = dict(Counter(topping))
    set_dic = set()
    
    for i in topping:
        dic[i] -= 1
        set_dic.add(i)
        if dic[i] == 0:
            dic.pop(i)
        if len(dic) == len(set_dic):
            answer += 1

    return answer