
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dictt = {}
        for string in strs:
            key = "".join(sorted(string))
            if key in dictt:
                dictt[key].append(string)
            else:
                dictt[key] = [string]

        return list(dictt.values())
        


