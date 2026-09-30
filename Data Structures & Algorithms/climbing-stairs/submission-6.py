class Solution:
    
    def climbStairs(self, n: int) -> int:
        memo = [-1]*(n+1)
        
        def fun(n):
            if n == 0:
                memo[0] = 1
                return 1
            elif n < 0:
                return 0
            else:     
                a = fun(n-1) if memo[n-1] == -1 else memo[n-1]
                b = fun(n-2) if memo[n-2] == -1 else memo[n-2]
                memo[n] = a + b
                return memo[n]
        return fun(n)
        

        
        

        