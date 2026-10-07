class Solution:
    def longestPalindrome(self, s: str) -> str:
        self.start,self.end = 0, 0
        
        def lG(l,r):
            if l < 0 or r >= len(s):
                return
            if s[l] != s[r]:
                return

            lG(l-1,r+1)

            if self.end - self.start < r - l:
                self.end = r
                self.start = l
        for i in range(len(s)):
            lG(i, i)
            lG(i, i + 1)
        return s[self.start:self.end+1]
            
        
            
        
        
            
            
                
            
             
        


        