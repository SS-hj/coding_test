def to_k_number(n, k):      # n을 k진수로 반환
    res = ""
    while n > 0:
        res += str(n % k)
        n = n //  k
    return ''.join(reversed(res))

def is_prime_num(k):        # 소수 구하기 (에라토스테네스의 체)
    if k == 2 or k == 3: 
        return True
    if k % 2 == 0 or k < 2: 
        return False 
    for i in range(3, int(k ** 0.5) + 1, 2):
        if k % i == 0:
            return False
    return True

def solution(n, k):
    answer = 0
    k_num = to_k_number(n, k)                   # 1. k진수로 반환
    for n in k_num.replace('0',' ').split():    # 2. 0을 포함하지 않는 수 p
        if is_prime_num(int(n)):                # 3. 소수인지
            answer += 1
    return answer