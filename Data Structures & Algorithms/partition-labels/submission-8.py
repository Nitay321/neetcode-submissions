class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        arr = [None]*26

        for i in range(len(s)):
            key = ord(s[i]) - ord("a")
            arr[key] = i    
            
        res = [0]
        farthest = 0
        seen = set()

        for curr, c in enumerate(s):
            if s[curr] in seen:
                res[len(res)-1] += 1
                continue
            key = ord(s[curr]) - ord("a") 
            
            if curr <= farthest:
                seen.add(s[curr])
                res[len(res)-1] += 1
            else:
                res.append(1)
                
            farthest = max(farthest, arr[key])


        return res


             
            


            


        
        



        