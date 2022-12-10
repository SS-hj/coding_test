def solution(elements):
    n = len(elements)
    elements *= 2
    temp = [sum(elements[i:i+length]) for i in range(n) for length in range(1,n+1)]
    return len(set(temp))