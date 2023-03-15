import re
class Solution:
    def isPalindrome(self, s: str) -> bool:
        p = re.compile('[a-z0-9]+')
        check = "".join(p.findall(s.lower()))
        return check == check[::-1]