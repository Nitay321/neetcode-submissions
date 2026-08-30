from collections import defaultdict
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        counter = defaultdict(int)
        for c in s:
            counter[c] += 1

        for c in t:
            if c not in t:
                return False
            counter[c] -= 1
            if counter[c] < 0:
                return False
        return True


