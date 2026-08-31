from collections import defaultdict
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l, r = 0, 0
        maxL = 0
        

        counter = defaultdict(int)

        while r<len(s):
            counter[s[r]]+=1
            window_length = r - l + 1
            max_value = 0
            for value in counter.values():
                if value > max_value:
                    max_value = value
            if window_length - max_value > k:
                counter[s[l]] -= 1
                l+=1
            else:
                maxL = max(maxL, window_length)
            r+=1
           
            
        return maxL
                

        
        
  
     

        