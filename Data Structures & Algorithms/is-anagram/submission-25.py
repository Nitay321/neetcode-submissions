class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        dictt = {}
        for c in s:
            dictt[c] = dictt.get(c,0) + 1
        
        for c in t:
            if c not in dictt:
                return False
            dictt[c] -= 1
            if dictt[c] < 0:
                return False
        for val in dictt.values():
            if val > 0:
                return False
        return True
        