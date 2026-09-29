from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dictt = defaultdict(list)
        res = []
        for string in strs:
            key = [0]*26
            
            for char in string:
                index = ord(char) - ord("a")
                key[index] += 1

            dictt[tuple(key)].append(string)
        
        return list(dictt.values())
            

            
        