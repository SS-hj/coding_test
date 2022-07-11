import re
import math
def solution(str1, str2):
    p = re.compile('[a-z][a-z]')
    str1 = str1.lower()
    str2 = str2.lower()
    check1 = []
    check2 = []
    for i in range(len(str1)-1):
        temp = p.match(str1[i:i+2])
        if temp:
            check1.append(temp.group())
    for i in range(len(str2)-1):
        temp = p.match(str2[i:i+2])
        if temp:
            check2.append(temp.group())
    print(check1)
    print(check2)
    if len(check1) == 0:
        if len(check2) == 0: answer = 65536
        else: answer = 0    
    else:
        cnt = 0
        total = len(check1)+len(check2)
        for i in check1:
            if i in check2:
                cnt += 1
                check2.remove(i) 
        print(cnt)
        answer = math.floor((cnt/(total-cnt))*65536)
    return answer