def solution(number, k):
    answer = []
    for num in number:
        # 스택의 마지막 값이 push 할 값보다 작다면 크거나 같은 값이 나올 때까지 값들에 대해서 pop
        while k > 0 and answer and answer[-1] < num: # 적절한 조건문
            answer.pop()
            k -= 1
        answer.append(num)
    return ''.join(answer[:len(answer) - k])