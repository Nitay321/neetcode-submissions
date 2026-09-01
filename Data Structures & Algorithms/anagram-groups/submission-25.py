from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dictt = defaultdict(list)
        for s in strs:
            counter = [0] * 26
            for c in s:
                index = ord(c)-ord("a")
                counter[index] += 1
            dictt[tuple(counter)].append(s)
        return list(dictt.values())
            
        


