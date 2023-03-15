class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        for c in 'abcdefghijklmnopqlstuvwxyz':
            if s.count(c)!=t.count(c):
                return False
        return True