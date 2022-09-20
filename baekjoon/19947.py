h, y = map(int,input().split())

def calc(h, y):
    if y == 0:
        return h
    else:
        if y >= 5:
            max(calc(h*1.35, y-5),calc(h*1.2, y-3),calc(h*1.05, y-1))
        if y >= 3:
            max(calc(h*1.2, y-3),calc(h*1.05, y-1))
        if y < 3:
            calc(h*1.05, y-1)
        return h
        
print(calc(h, y))
