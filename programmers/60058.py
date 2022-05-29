# if "균형잡힌 괄호 문자열", then return True
def isBanlancedString(str):
    return str.count('(') == str.count(')')

# if "올바른 괄호 문자열", then return True
def isCorrectString(str):
    count = 0
    for s in str:
        if s == '(':
            count += 1
        else: # ')'
            count -= 1
        if count < 0:
            return False
    return count == 0

def process(str):
    # 1. 입력이 빈 문자열인 경우, 빈 문자열을 반환합니다.
    if str == "":
        return ""
    # 2. 문자열 w를 두 "균형잡힌 괄호 문자열" u, v로 분리합니다. 단, u는 "균형잡힌 괄호 문자열"로 더 이상 분리할 수 없어야 하며, v는 빈 문자열이 될 수 있습니다.
    u, v = splitUV(str)
    print(u, v)
    # 3. 문자열 u가 "올바른 괄호 문자열" 이라면 문자열 v에 대해 1단계부터 다시 수행합니다.
    #   3-1. 수행한 결과 문자열을 u에 이어 붙인 후 반환합니다.
    if isCorrectString(u):
        u += process(v)
        return u
    else: # 4. 문자열 u가 "올바른 괄호 문자열"이 아니라면 아래 과정을 수행합니다.
    #   4-1. 빈 문자열에 첫 번째 문자로 '('를 붙입니다.
        newStr = "("
    #   4-2. 문자열 v에 대해 1단계부터 재귀적으로 수행한 결과 문자열을 이어 붙입니다.
        newStr += process(v)
    #   4-3. ')'를 다시 붙입니다.
        newStr += ")"
    #   4-4. u의 첫 번째와 마지막 문자를 제거하고, 나머지 문자열의 괄호 방향을 뒤집어서 뒤에 붙입니다.
        if len(u) > 0:
            newStr += reverseStr(u[1:-1])
    #   4-5. 생성된 문자열을 반환합니다.
        return newStr

def reverseStr(str):
    ans = ""
    for s in str:
        if s == "(":
            ans += ")"
        else:
            ans += "("
    return ans

# 2. 문자열 w를 두 "균형잡힌 괄호 문자열" u, v로 분리합니다. 단, u는 "균형잡힌 괄호 문자열"로 더 이상 분리할 수 없어야 하며, v는 빈 문자열이 될 수 있습니다.
def splitUV(str):
    u, v = str, ""
    for i in range(2, len(str), 2):
        if isBanlancedString(str[:i]):
            u = str[:i]
            v = str[i:]
            break
    return u, v

def solution(p):
    p = p.strip()

    if isCorrectString(p): # 이미 올바른 괄호 문자열이라면 그대로 return
        return p

    return process(p)
