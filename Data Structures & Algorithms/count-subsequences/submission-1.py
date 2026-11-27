class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        if len(s) < len(t):
            return 0

        dp = {}
        
        def dfs(i,j):
            if (i,j) in dp:
                return dp[(i,j)]
            if j == len(t):
                return 1
            if i == len(s):
                return 0      
            A = dfs(i+1,j+1) if s[i] == t[j] else 0
            B = dfs(i+1,j)

            dp[(i,j)] = A+B
            return dp[(i,j)]

        return dfs(0,0)



            

        