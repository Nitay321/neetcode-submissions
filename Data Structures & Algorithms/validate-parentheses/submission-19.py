class Solution:
    def isValid(self, s: str) -> bool:
       if len(s) % 2 != 0:
          return False

       stack = []
       for ch in s:
         if len(stack) == 0:
            if ch in ["]","}",")"]:
                return False
            else:
                stack.append(ch)
         else:
            if ch in ["[","{","("]:
                stack.append(ch)
            else:
                bracket = stack.pop()
                if bracket == "[" and ch != "]":
                    return False
                if bracket == "{" and ch != "}":
                    return False
                if bracket == "(" and ch != ")":
                    return False
       return len(stack) == 0
                
            

                
            
        