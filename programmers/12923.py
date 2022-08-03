def solution(begin, end):
    answer = []
    for i in range(begin, end+1):
        k = int(i != 1)  # i가 1이면 0, 1이 아니면 1을 대입
        # 약수를 구하기
        # 2~sqrt(n)까지 순회하며 n과 나누어 떨어지는 수가 그 약수
        for j in range(2, int(i**0.5)+1): # i**0.5 == sqrt(i)
            if i%j == 0 and i//j <= 10000000: # + 숫자 블럭의 최대 값 조건
                k = i//j  # i//j가 약수 중 가장 큰 값
                break
        answer.append(k)
    
    return answer