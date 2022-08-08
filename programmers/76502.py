def solution(s):
    answer = 0 ; temp = list(s)
    for _ in range(len(s)):
        st = [] # 여는 괄호들만 넣을 stack
        # stack이어야 문제의 조건에 부합하게된다. 
        # 가장 최근의 괄호끼리 세트가 맞아야되기 때문
        for i in range(len(temp)):
            if len(st) > 0: # 0보다 커야 괄호의 순서가 맞는 것
                if st[-1] == '[' and temp[i] == ']':
                    st.pop()
                elif st[-1] == '(' and temp[i] == ')':
                    st.pop()
                elif st[-1] == '{' and temp[i] == '}':
                    st.pop()
                else:
                    st.append(temp[i])
            else:
                st.append(temp[i])
        if len(st) == 0:
            answer += 1
        temp.append(temp.pop(0)) # s를 로테이션하면서 확인
    return answer