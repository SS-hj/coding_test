def solution(numbers):
    if sum(numbers) == 0: return '0'
    return ''.join(sorted(list(map(str,numbers)), key = lambda x : x*3, reverse = True))