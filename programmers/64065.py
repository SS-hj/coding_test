from collections import Counter
def solution(s):
    new_s = [sss.replace('{','').replace('}','') for sss in s.split(',')]
    # collections.Counter(a).most_common() : a의 요소를 세어, 리스트로 반환
    # 이렇게 나온 결과를 빈도수를 기준으로 원소를 내림차순 정렬
    return [int(c[0]) for c in sorted(Counter(new_s).most_common(), key = lambda x: -x[1])]