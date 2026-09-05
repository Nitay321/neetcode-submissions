class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        closed = {"(": ")", "{": "}", "[": "]"}
        for c in s:
            if c in ["[","(","{"]:
                stack.append(c)
            else:
               if not stack:
                    return False
               bracket = stack.pop()
               if closed[bracket] != c:
                    return False
        return not stack
