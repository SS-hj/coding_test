class Solution:
    def addBinary(self, a: str, b: str) -> str:
        a, b = list(a), list(b)
        res = ''
        temp = 0
        for i in range(max(len(a),len(b))):
            i = int(a.pop()) if a else 0
            j = int(b.pop()) if b else 0
            res = str((i+j+temp)%2)+res
            temp = (i+j+temp)//2
        return f'1{res}' if temp else res