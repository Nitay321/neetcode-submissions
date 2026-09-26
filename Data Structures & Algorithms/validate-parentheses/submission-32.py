class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        dictt = {"(":")", "{":"}", "[":"]"}
        for c in s:
            if c in ["{","(","["]:
                stack.append(c)
            else:
                if not stack:
                    return False
                element = stack.pop()
                if dictt[element] != c:
                    return False
        return not stack


                