class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        counter = {}
        for c in s:
            counter[c] = 1 + counter.get(c,0)
        print(counter)
        for c in t:
            if c in counter:
                counter[c] -= 1
        
        print(counter)
        for value in counter.values():
            if value != 0:
                return False

        return True
        