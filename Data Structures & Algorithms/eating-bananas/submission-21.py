import math
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, 0
        
        for pile in piles:
            r = max(pile, r)

        min_k = r
        while l <= r:
            k = (l + r) // 2
            copy_h = h

            for pile in piles:  
                copy_h -= (math.ceil(pile/k))
                if copy_h < 0:
                    
                    break

            if copy_h < 0:
                    l = k + 1
            else:
                min_k = min(min_k, k)
                r = k - 1


        return min_k





        