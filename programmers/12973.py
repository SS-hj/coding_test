def solution(s): 
    stack = []
    for i in s:
        # stack 에 아무것도 없으면 append
        if len(stack) == 0: stack.append(i) 
        # 현재 문자열 i 와 이전에 stack 처리한 문자와 동일하면 stack에 있던거 빼기
        elif stack[-1] == i: stack.pop() 
        else: stack.append(i)
    if len(stack) == 0: return 1
    else: return 0