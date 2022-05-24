x = input()

cnt = 1
def sum_digit(x):
    global cnt
    arr = list(map(int,x))
    temp = sum(arr)
    if len(str(temp)) == 1:
        print(cnt)
        if temp in [3,6,9]:
            print('YES')
        else:
            print('NO')
    else:
        cnt += 1
        sum_digit(str(temp))
        
if len(x) == 1:
    print(0)
    if int(x) in [3,6,9]:
        print('YES')
    else:
        print('NO')
else:
    sum_digit(x)