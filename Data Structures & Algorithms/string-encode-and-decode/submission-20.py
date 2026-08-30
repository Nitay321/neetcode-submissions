class Solution:

    def encode(self, strs: List[str]) -> str:
        result = []
        for string in strs:
            result.append(str(len(string)) + "#" + string)
        return "".join(result)

    def decode(self, s: str) -> List[str]:
        result = []
        i=0
        j=0
        while j < len(s):
            if s[j] == "#":
                length = int(s[i:j])
                result.append(s[j+1:j+1+length])
                i=j+1+length
                j=i
            j+=1
        return result





            
            


