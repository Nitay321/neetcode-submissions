class Solution:
    def countSubstrings(self, s: str) -> int:

        def cS(l,r):
            if l<0 or r>=len(s):
                return 0
            if s[l] != s[r]:
                return 0
            
            return 1 + cS(l-1,r+1)
        
        count = 0
        for i in range(len(s)):
            count += cS(i,i)
            count += cS(i,i+1)
        return count

            
        