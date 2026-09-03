class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l = 0
        freq = {}
        max_freq = 0
        max_length = 0
        for r,c in enumerate(s):
            freq[c] = freq.get(c,0) + 1
            max_freq = max(max_freq, freq[c])
            length = r-l+1
            if length - max_freq > k:
                freq[s[l]] -= 1
                l += 1
            else:
                max_length = length
        return max_length
            

        