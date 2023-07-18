import sys
input = sys.stdin.readline

s = input().strip()
n = int(input())
check = [[0]*26 for _ in range(len(s))]
for i in range(len(s)):
    for j in range(26):
        if ord(s[i])-97==j:
            check[i][j] = check[i-1][j]+1
        else:
            check[i][j] = check[i-1][j]
for _ in range(n):
    a, i, j = input().split()
    if int(i)==0:
        print(check[int(j)][ord(a)-97])
    else:
        print(check[int(j)][ord(a)-97]-check[int(i)-1][ord(a)-97])