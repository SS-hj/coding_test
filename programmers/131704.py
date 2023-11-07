def solution(order):
    stack = []
    idx = 0
    for num in range(1, len(order)+2):
        while stack and stack[-1] == order[idx]:
            idx += 1
            stack.pop()
        stack.append(num)
    return idx