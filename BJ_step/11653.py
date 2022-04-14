n = int(input())

arr = []
i = 2
if n > 1:
    while i < n :
        if n % i == 0:
            while n % i == 0:
                arr += [i]
                n = n//i
        i += 1
    if n > 1:
        arr += [n]
    
for k in arr:
    print(k)