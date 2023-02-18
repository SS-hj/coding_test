def solution(n, t, m, p):
    def calc(num):
        result = []
        while num > 0:
            if num % n < 10:
                result.append(num % n)
            else:
                result.append(chr(num % n + 55))
            num //= n
        return result[::-1]
    
    temp = [0]
    num = 1
    while len(temp) < t*m:
        temp.extend(calc(num))
        num += 1
    
    return ''.join(map(str, temp))[p-1::m][:t]