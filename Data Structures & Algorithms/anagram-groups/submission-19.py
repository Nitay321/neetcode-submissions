from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dictt = defaultdict(list)
        for string in strs:
            counter = [0]*26
            for char in string:
                index = ord(char)-ord("a")
                counter[index] += 1
            key = tuple(counter)
            dictt[key].append(string)
        return list(dictt.values())
        