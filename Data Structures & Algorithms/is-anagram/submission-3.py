class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        histogram = {}
        for char in s:
            if char in histogram:
                histogram[char]+=1
            else:
                histogram[char] = 1
        
        for char in t:
            if char in histogram and histogram[char] != 0:
                  histogram[char] -= 1
                  if histogram[char] == 0:
                     histogram.pop(char)
            else:
                return False
        
        return histogram == {}
        