n = int(input())
arr = []
for k in range(n):
    arr += [list(input())]
    
total = 0
for w in arr:
    gr = True
    j = 0
    while j < len(w):
        cnt = w.count(w[j])
        if cnt == 1:
            j += 1
            continue
        else:
            for k in range(1,cnt+1):
                if w[j] != w[j+k-1]:
                    gr = False
                    break
            j += cnt
        if gr == False:
            break
    if gr != False:
        total += 1
print(total)