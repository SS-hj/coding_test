def solution(s):
    answer = []
    for string in s:
        stack = []
        count_110 = 0
        for str in string:
            # 110이 나온 경우
            if len(stack) >= 2 and stack[-2:] == ["1","1"] and str == '0':
                count_110 += 1
                stack.pop()
                stack.pop()
            else:
                stack.append(str)

        # 110을 모두 제거했으므로 남은 문자열에서 연속된 1이 존재하는 곳은 한 곳밖에 없다.
        count_1 = 0
        for s in stack[::-1]:
            if s == '0':    # 가장 마지막 0 부터 110들을 넣어줌
                break
            else:
                count_1 += 1
        answer.append(''.join(stack[:len(stack) - count_1]) + '110' * count_110 + '1' * count_1)
    return answer