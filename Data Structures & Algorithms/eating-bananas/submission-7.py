import math

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        max_pile = 0
        for pile in piles:
            if max_pile < pile:
                max_pile = pile

        l = 1
        r = max_pile
        min_k = None
        while l<=r:
            k = (l+r) // 2
            c_h = h

            for i, pile in enumerate(piles):
                c_h = c_h - math.ceil(pile / k)
                if i == len(piles)-1:
                    if c_h < 0: 
                        l = k + 1
                    else:
                        min_k = k
                        r = k - 1
                        
                elif c_h <= 0:
                    l = k + 1
                    break
           
        return min_k 


            



        