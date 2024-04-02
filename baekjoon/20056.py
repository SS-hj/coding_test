n, m, k = map(int, input().split())
info = []
for _ in range(m):
    r,c,g,s,d = map(int, input().split())
    info.append((r-1,c-1,g,s,d))

dr = [-1,-1,0,1,1,1,0,-1]
dc = [0,1,1,1,0,-1,-1,-1]

while k>0:
    check = {}
    while info:
        r,c,g,s,d = info.pop()
        nr, nc = (r+dr[d]*s+n)%n, (c+dc[d]*s+n)%n
        if (nr, nc) in check:
            check[(nr, nc)][0] += g
            check[(nr, nc)][1] += s
            check[(nr, nc)][2].append(d)
        else:
            check[(nr, nc)] = [g, s, [d]]
    for (r, c) in check:
        g,s,d = check[(r,c)]
        t = len(d)
        if t>1:
            if g>=5:
                fist_d = d[0]
                for z in d:
                    if fist_d%2!=z%2:
                        for direct in range(1,8,2):
                            info.append((r,c,g//5,s//t,direct))
                        break
                else:
                    for direct in range(0,7,2):
                        info.append((r,c,g//5,s//t,direct))
        else:
            info.append((r,c,g,s,d[0]))
    k -= 1
    
print(sum(g for _,_,g,_,_ in info))