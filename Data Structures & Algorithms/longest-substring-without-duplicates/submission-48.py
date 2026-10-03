class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        dictt = {}
        maxL = 0

        for r in range(len(s)):
            if s[r] in dictt:
                l = max(l, dictt[s[r]] + 1)
            dictt[s[r]] = r
            maxL = max(maxL, r - l + 1)
        return maxL
        

