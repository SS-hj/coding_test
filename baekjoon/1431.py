from unittest import skip


n = int(input())
arr = []
for i in range(n):
    serial = input()
    sum = 0
    for s in serial:
        try: sum += int(s)
        except: continue
    arr.append([serial,sum])
arr.sort(key = lambda x: (len(x[0]), x[1], x[0]))
for a in arr:
    print(a[0])