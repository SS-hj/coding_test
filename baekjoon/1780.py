n = int(input())
arr = [list(map(int,input().split())) for _ in range(n)]

minusCnt = 0
zeroCnt = 0
oneCnt = 0

def cut(test):
    global minusCnt
    global zeroCnt
    global oneCnt
    
    val = test[0][0]
    check = False
    for i in range(len(test)):
        for j in range(len(test)):
            if test[i][j] != val:
                check = True
                break
        if check:
            break
    if check:
        num = len(test) // 3 
        cut([test[i][:num] for i in range(num)])
        cut([test[i][num:2*num] for i in range(num)])
        cut([test[i][2*num:] for i in range(num)])
        cut([test[i][:num] for i in range(num,2*num)])
        cut([test[i][num:2*num] for i in range(num,2*num)])
        cut([test[i][2*num:] for i in range(num,2*num)])
        cut([test[i][:num] for i in range(2*num,3*num)])
        cut([test[i][num:2*num] for i in range(2*num,3*num)])
        cut([test[i][2*num:] for i in range(2*num,3*num)])
    else:
        if val < 0: minusCnt += 1
        elif val == 0: zeroCnt += 1
        else: oneCnt += 1
cut(arr)

print(minusCnt)
print(zeroCnt)
print(oneCnt)