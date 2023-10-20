def solution(msg):
    check = dict(zip('ABCDEFGHIJKLMNOPQRSTUVWXYZ',range(1,27)))
    n = len(msg)
    answer = []
    idx = 27
    while msg:
        e = 1
        while msg[:e+1] in check and e+1<=len(msg):
            e+=1
        answer.append(check[msg[:e]])
        check[msg[:e+1]] = idx
        idx += 1
        msg = msg[e:]
    return answer