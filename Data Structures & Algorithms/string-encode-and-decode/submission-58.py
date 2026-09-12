from typing import List

class Solution:

    def encode(self, strs: List[str]) -> str:
        res = []
        for string in strs:
            res.append(str(len(string)) + "#" + string)
        return "".join(res)

    def decode(self, s: str) -> List[str]:
        l = 0
        res = []
        
        while l < len(s):
            r = s.find("#", l)
            length = int(s[l:r])
            
            l = r + 1
            r = l + length
            res.append(s[l:r])
            
            l = r

        return res