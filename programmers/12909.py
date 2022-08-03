def solution(s):
    x = 0
    for w in s:
        if x < 0: # 괄호부터 여므로, 항상 "(" 의 개수가 더 많아야 한다
            break
        x = x+1 if w=="(" else x-1
    return x==0