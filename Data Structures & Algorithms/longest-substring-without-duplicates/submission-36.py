class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        dictt = {}
        maxL = 0
        for r,c in enumerate(s):
            if c not in dictt:
                dictt[c] = r
            else:
                l = max(l,dictt[c] + 1)
            dictt[c] = r
            length = r - l + 1
            if length > maxL:
                    maxL = length

        return maxL


        

        