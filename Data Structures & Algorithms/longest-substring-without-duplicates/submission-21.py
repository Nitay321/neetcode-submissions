class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l,r = 0, 0
        maxL = 0
        dictt = {}
        
        while r < len(s):
            if s[r] not in dictt:
                dictt[s[r]] = r
                
            else:
                l = max(l, dictt[s[r]] + 1)    
                dictt[s[r]] = r
                
            length = r - l + 1
            maxL = max(maxL, length)
            r += 1
        return maxL
                


            
