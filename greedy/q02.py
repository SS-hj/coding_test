arr = list(input())

res = int(arr[0])
for i in range(1,len(arr)):
    num = int(arr[i])
    if res * num >= res + num:
        res *= num
    else:
        res += num

print(res)