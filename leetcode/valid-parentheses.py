class Solution(object):
    def isValid(self, s):
        Map={")":"(","}":"{","]":"["}
        stack=[]
        for c in s:
            if c in Map:
                if stack and stack[-1]==Map[c]:
                   stack.pop()
                else:
                    return False
            else:
                stack.append(c)
        return False if stack else True