class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        
        for token in tokens:
            if token in ["+","*","/","-"]:
                val2 = int(stack.pop())
                val1 = int(stack.pop())
                res = 0
                if token == "+":
                    res = val1 + val2
                elif token == "-":
                    res = val1 - val2
                elif token == "*":
                    res = val1 * val2
                else:
                    res = val1 / val2
                stack.append(res)
            else:
                stack.append(token)
        return int(stack.pop())
            
        


        # (3 + 4) × (5 + 6) becomes 3 4 + 5 6 + × 