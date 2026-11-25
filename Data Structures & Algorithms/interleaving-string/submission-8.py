class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        if len(s1)+len(s2) != len(s3):
            return False
        
        if not s1 or not s2:
            if s1 == s3 or s2 == s3:
                return True
            return False
        
        dp = {}

        def dfs(i,j):
            if (i,j) in dp:
                return dp[(i,j)]
            if i + j == len(s3):
                dp[(i,j)] = True
                return True

            res = False
            if i < len(s1) and s1[i] == s3[i+j]:
                res = dfs(i+1, j)
            if j < len(s2) and s2[j] == s3[i+j] and not res:
                res = dfs(i, j+1)
            
            dp[(i,j)] = res
            return res
               
        return dfs(0,0)
            

                
                

        