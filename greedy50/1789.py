s = int(input())

cnt = 0
num = s

# point; N개가 몇인지 알면 되는 것. 실제 합이 되는 자연수 원소는 알 필요 x
for i in range(1,s+1):
    if num - i == 0:
        cnt += 1 
        print(cnt)
        break
    elif num - i > 0:
        num -= i
        cnt += 1
        continue
    else:
        print(cnt)
        break