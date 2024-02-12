s = input()
boom = list(input())
n = len(boom)
stack = []

for letter in s:
    stack.append(letter)
    if len(stack)>=n and stack[-n:]==boom:
        for _ in range(n):
            stack.pop()

print("".join(stack) if stack else "FRULA")