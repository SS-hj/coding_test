w = input()
stack = []      # 몇번째 인덱스에 여는 괄호가 있는지
res = list(w)   # 원래 인덱스에 있던 문자열이 변환된 후

for i in range(len(w)):
    if w[i]=="(":
        stack.append(i)
    elif w[i]==")":
        s = stack.pop()
        res[s-1] = int(res[s-1])*"".join(res[s+1:i])    # 압축해제 결과
        for j in range(s,i+1):
            res[j] = "" # 압축해제 처리

print(len("".join(res)))