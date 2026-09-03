class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for token in tokens:
            if token in ["+","-","/","*"]:
                n2 = int(stack.pop())
                n1 = int(stack.pop())
                num = 0
                if token == "+":
                    num = n1 + n2
                elif token == "-":
                     num = n1 - n2
                elif token == "*":
                     num = n1 * n2
                else:
                     num = n1 / n2
                stack.append(num)
            else:
                stack.append(token)
        return int(stack.pop())

            
        