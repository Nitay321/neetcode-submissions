from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dictt = defaultdict(list)
        for string in strs:
            count = [0] * 26
            for char in string:
                index = ord(char)-ord('a')
                count[index] += 1
            key = tuple(count)
            dictt[key].append(string)
       
        return list(dictt.values())



        





        # dictt = {}
        # for string in strs:
          #  key = "".join(sorted(string))
           # if key in dictt:
            #    dictt[key].append(string)
            # else:
            #  dictt[key] = [string]

        # return list(dictt.values())
        


