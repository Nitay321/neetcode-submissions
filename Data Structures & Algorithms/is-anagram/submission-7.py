class Solution:
    
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t): ## checking for the same length
            return False

        count = {}
        for char in s:  # building Counter
            count[char] = count.get(char,0) + 1

        for char in t: # because lenghts are equel no worried for   count[char] < 0 at the end
            if char not in count or count[char] == 0:
                return False;
            count[char] -= 1

        return True