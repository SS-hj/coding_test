s = input()
list = ['c=','c-','dz=','d-','lj','nj','s=','z=']

cnt = 0
length = len(s)
for i in range(len(s)):
    for k in list:
        if k == s[i:i+3]:
            length -= 1
        elif k == s[i:i+2]:
            cnt += 1
            length -= 2        
    
print(cnt+length)