n, r, c = map(int,input().split())
arr = [[0]*(2**n) for _ in range(2**n)]
ans = str(r)+str(c)
arr[r][c] = ans

idx = 0
def visit(size, test):
    global idx
    if size == 0:
        if test[0][0] == ans:
            print(idx)
            return
        idx += 1
    else:
        num = len(test) // 2
        visit(size-1, [test[i][:num] for i in range(num)])
        visit(size-1, [test[i][num:2*num] for i in range(num)])
        visit(size-1, [test[i][:num] for i in range(num,2*num)])
        visit(size-1, [test[i][num:2*num] for i in range(num,2*num)])

visit(n, arr)