class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        memo = {}
    
        text1_length = len(text1)
        text2_length = len(text2)
        
        def lCS(i,j):
            if i == text1_length or j == text2_length:
                return 0
            if text1[i] == text2[j]:
                if (i+1,j+1) not in memo:
                    memo[(i+1,j+1)] = lCS(i+1,j+1)
                memo[(i,j)] = 1 + memo[(i+1,j+1)]
            else:
                if (i+1,j) not in memo:
                    memo[(i+1,j)] = lCS(i+1,j)
                if (i,j+1) not in memo:
                    memo[(i,j+1)] = lCS(i,j+1)
            
                memo[(i,j)] = max(memo[(i,j+1)],memo[(i+1,j)])   
                     
            return memo[(i,j)]

        return lCS(0,0)
                
            
        