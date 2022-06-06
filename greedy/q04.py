from itertools import combinations

n = int(input())
arr = list(map(int,input().split()))
arr.sort()
'''
타겟 금액 = 지금까지 만들었던 금액 + 현재 처리할 금액
위 식을 통해 가장 작은 금액부터 만들 수 있는 금액들을 처리하면서, 
타겟이 되는 금액을 업뎃하면서 확인한다.
'''

target = 1
for x in arr:
    if target < x:
        break
    target += x
print(target)