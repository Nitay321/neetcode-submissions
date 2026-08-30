class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        mapp = {")": "(", "}": "{", "]": "["}

        for c in s:
            if c in ["(", "{", "["]:
                stack.append(c)
            else:
                if not stack:
                    return False
                bracket = stack.pop()
                if mapp[c] != bracket:
                    return False
        return not stack

        