class Solution:

    def encode(self, strs: List[str]) -> str:
        res = []
        for string in strs:
            res.append(str(len(string)) + "#" + string)
        return "".join(res)
    def decode(self, s: str) -> List[str]:
        res = []
        i = 0
        # 5#Hello5#World
        # 0123456789

        while i<len(s):
            j = s.find("#",i) 
            length = int(s[i:j])
            string = s[j+1:j+length+1]
            res.append(string)
            i = j+length+1
        
        return res
            

