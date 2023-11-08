def solution(numbers):
    answer = []
    for number in numbers:
        bin_number = '0'+format(number, 'b')
        idx = bin_number.rfind('0')
        bin_number = bin_number[:idx]+'1'+bin_number[idx+1:]
        if number % 2 == 1:
            bin_number = bin_number[:idx+1]+'0'+bin_number[idx+2:]
        answer.append(int(bin_number, 2))
    return answer