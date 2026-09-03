import math
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        max_pile = 0
        for pile in piles:
            if pile > max_pile:
                max_pile = pile

        min_k = max_pile
        l, r = 1, max_pile
        
        while l<=r:
            k = (l + r) // 2
            copy_h = h
            for pile in piles:
                times = math.ceil(pile / k)
                copy_h -= times
                if copy_h < 0:
                    break 
            if copy_h < 0:
                l = k+1
            else:
                min_k = k
                r = k-1

        return min_k


                

                
        
        