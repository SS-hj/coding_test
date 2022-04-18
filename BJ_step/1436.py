n = int(input())
cnt = 0
six_n = 666
while True:
    if '666' in str(six_n): # 666을 포함하는 숫자중에서 몇 번째 숫자인가
        cnt += 1
    if cnt == n:
        print(six_n)
        break
    six_n += 1