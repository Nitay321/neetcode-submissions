class Solution:
    def longestPalindrome(self, s: str) -> str:
        self.start, self.end = 0, 0
        
        def lG(l, r):
            # 1. Base case: out of bounds
            if l < 0 or r >= len(s):
                return
            
            # 2. Base case: not a palindrome anymore, stop expanding
            if s[l] != s[r]:
                return
                
            # 3. Since s[l] == s[r], this IS a valid palindrome.
            # Check if it's the longest we've seen so far.
            if r - l > self.end - self.start:
                self.start = l
                self.end = r
                
            # 4. Expand outwards on BOTH sides simultaneously
            lG(l-1, r+1)

        # We must try expanding from EVERY character in the string
        for i in range(len(s)):
            lG(i, i)       # Try expanding assuming a 1-character center (e.g., "aba")
            lG(i, i+1)     # Try expanding assuming a 2-character center (e.g., "abba")
            
        return s[self.start:self.end+1]