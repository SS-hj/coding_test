T = int(input())

# 보물 상자에 적힌 숫자로 만들 수 있는 모든 수 중, K번째로 큰 수를 10진 수로 만든 수
for t in range(1, T + 1):
    N, k =map(int,input().split())
    s = input()
    e = len(s)//4 # e씩 s를 나누어야 한다.
    temp = []
    for i in range(e):
        idx = list(range(i,len(s),e))
        temp.append(s[idx[0]:idx[1]])
        temp.append(s[idx[1]:idx[2]])
        temp.append(s[idx[2]:idx[3]])
        temp.append(s[idx[3]:]+s[:i])
    temp = list(set(temp))
    tmp = []
    for j in temp:
        tmp += [int(j, 16)] # 16진수로 표현된 j를 10진수로 
    tmp.sort(reverse=True)
    print('#'+str(t), tmp[k-1])