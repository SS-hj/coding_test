n = int(input())
for _ in range(n):
    s = input()
    m = len(s)
    check, idx = 0, 0
    while check>=0 and idx<m:
        if s[idx]=="(":
            check += 1
        else:
            check -= 1
        idx += 1
    print("YES" if check==0 else "NO")