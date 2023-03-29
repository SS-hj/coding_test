class Solution:
    def longestPalindrome(self, s: str) -> int:
        check = {}
        res = 0
        for v in s:
            if v not in check:
                check[v] = 1
            else:
                check[v] += 1
        for value in check.values():
            res += value // 2 * 2
        return min(res+1,len(s))