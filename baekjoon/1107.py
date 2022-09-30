num = int(input())
err = []
if int(input()):
    err = input().split()

res = 1e9
for i in range(1000001):
    for j in str(i):
        if j in err:
            break
    else: # 고장나지 않은 버튼으로 누른 채널
        res = min(abs(i-num)+len(str(i)),res) # 채널 수의 차이 + i 채널로 가기위한 버튼수
        
# 100번에서 num까지 가는 게 더 빠른 경우를 고려 (예외처리)
res = min(abs(100-num),res)
print(res)
