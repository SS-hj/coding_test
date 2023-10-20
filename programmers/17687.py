def solution(n, t, m, p):
    num_to_chr = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "A", "B", "C", "D", "E", "F"]
    def to_k_number(n, k):      # n을 k진수로 반환
        res = ""
        while n > 0:
            res = num_to_chr[n % k] + res
            n = n // k
        return res
    s = "0"
    num = 1
    while len(s)<m*t:
        s = s+to_k_number(num,n)
        num+=1
    return s[p-1::m][:t]