def recursion(arr, start, cur_l):
    tmp=cur_l//3
    if tmp==0:
        return
    for i in range(start+tmp, start+tmp*2):
        arr[i]=' '
    recursion(arr, start, tmp)
    recursion(arr, start+tmp*2, tmp)
while True:
    try:
        n=int(input())
        if n=='':
            break
        arr=['-' for _ in range(3**n)]
        recursion(arr, 0, 3**n)
        answer=''.join(arr)
        print(answer)
    except EOFError:
        break