class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        l = 0
        dictt = {}

        for c in s1:
            dictt[c] = dictt.get(c,0) + 1

        for r in range(len(s2)):
            if s2[r] not in dictt:
                while l < r:
                    dictt[s2[l]] += 1
                    l += 1
                l += 1
            elif dictt[s2[r]] == 0:
                while s2[l] != s2[r]:
                    dictt[s2[l]] += 1
                    l += 1   
                l+=1                     
            else:
                dictt[s2[r]] -= 1
            
            if r-l+1 == len(s1):
                return True

        return False
                
                
        




            
        

        

        