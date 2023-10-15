def solution(str1, str2):
    check = dict()
    total = 0
    for i in range(len(str1)-1):
        s = str1[i:i+2].lower()
        if s.isalpha():
            total += 1
            if s in check:
                check[s] += 1
            else:
                check[s] = 1
    nset = 0
    for i in range(len(str2)-1):
        s = str2[i:i+2].lower()
        if s.isalpha():
            if s in check:
                nset += 1
                check[s] -= 1
                if check[s] == 0:
                    del check[s]
            else:
                total += 1
    res = 1 if total==nset else nset/total
    return int(res*65536)