class Solution:
    def encode(self, strs: list[str]) -> str:
        res = []
        for string in strs:
            res.append(str(len(string)) + "#" + string)
        return "".join(res)

    def decode(self, s: str) -> list[str]:
        res = []
        i = 0
        
        while i < len(s):
            # Find the delimiter '#' starting directly from the current number position
            j = s.find("#", i)
            
            # Extract the length
            length = int(s[i:j])
            
            # Slice the exact string using the parsed length
            word = s[j + 1 : j + 1 + length]
            res.append(word)
            
            # Jump past this word to the start of the next length prefix
            i = j + 1 + length
            
        return res