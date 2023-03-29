class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        for s in set(ransomNote):
            if magazine.count(s) < ransomNote.count(s):
                return False
        return True