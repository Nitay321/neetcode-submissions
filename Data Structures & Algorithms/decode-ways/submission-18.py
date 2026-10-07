class Solution:
    def numDecodings(self, s: str) -> int:
        memo = {}
        def dD(i):
            if i == len(s):
                return 1 
            a = int(s[i])
            if a == 0:
                memo[i] = 0
                return memo[i]
            if i+1 == len(s):
                if i not in memo:
                    memo[i] = dD(i+1)
                return memo[i]  
            
            b = int(s[i] + s[i+1])

            if i+1 not in memo:
                memo[i+1] = dD(i+1)
            if i+2 not in memo:
                memo[i+2] = dD(i+2)
            if 1<=b<=26:
                memo[i] = memo[i+1] + memo[i+2]
            else:
                memo[i] = memo[i+1]

            return memo[i]
        dD(0)
        return memo[0]
        
            

            

                



        