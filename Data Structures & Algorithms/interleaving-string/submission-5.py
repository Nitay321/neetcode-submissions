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

            dp[(i,j)] = False
            if i == len(s1):
                if s2[j] != s3[i+j]:
                    return False
                dp[(i,j)] = dfs(i, j+1)
            elif j == len(s2):
                if s1[i] != s3[i+j]:
                    return False
                dp[(i,j)] = dfs(i+1, j)
            else:
                ans1, ans2 = False, False
                if s2[j] == s3[i+j]:
                    ans1 = dfs(i, j+1)
                if s1[i] == s3[i+j]:
                    ans2 = dfs(i+1, j)
                
                dp[(i,j)] = ans1 or ans2

            return dp[(i,j)]

        return dfs(0,0)
            

                
                

        