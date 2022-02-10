s = list(map(int,input())) #한글자씩 리스트로

# 30의 배수가 되도록 하는 숫자 조합
# !!3의 배수는 각 자리 숫자의 합이 3의 배수인 수!!
s.sort(reverse=True)
if s[-1] != 0 or sum(s)%3 != 0:
    print(-1)

else:
    for k in s:
        print(k, end='')
