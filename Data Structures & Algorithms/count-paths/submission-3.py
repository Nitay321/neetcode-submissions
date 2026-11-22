class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        memo = {}
        m -= 1
        n -= 1
        def uP(i,j):
            print(i,j)
            if i > m or i<0 or j>n or j<0:
                memo[(i,j)] = 0
                return 0
            if m == i and n == j:
                memo[(i,j)] = 1
                return 1
            if (i+1,j) not in memo:
                memo[(i+1,j)] = uP(i+1,j)
            if (i,j+1) not in memo:
                memo[(i,j+1)] = uP(i,j+1)
            
            memo[(i,j)] = memo[(i+1,j)] + memo[(i,j+1)] 
            return memo[(i,j)]
        
        return uP(0,0)
            
            


