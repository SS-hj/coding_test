def solution(numbers):
    num = [0,1,2,3,4,5,6,7,8,9]
    for n in numbers:
        num.remove(n)
    answer = sum(num)
    return answer