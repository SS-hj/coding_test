n = int(input())
arr = []
for _ in range(n):
    temp = list(input().split())
    arr.append(temp[1:])
arr.sort()

checked = set() # (이전 val들 + val)
for a in arr:
    temp = ""
    for idx, val in enumerate(a):
        temp += val
        if temp not in checked:
            checked.add(temp)
            print("--"*idx+val)