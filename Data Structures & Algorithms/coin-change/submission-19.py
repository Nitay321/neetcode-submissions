import math
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dictt = {}

        def cC(i, a):
            if a == 0:
                dictt[(i,a)] = 0
                return 0
            if i == len(coins) or a < 0:
                dictt[(i,a)] = math.inf
                return math.inf
            x = cC(i+1,a) if (i+1,a) not in dictt else dictt[(i+1,a)]
            y = cC(i,a-coins[i]) if (i,a-coins[i]) not in dictt else dictt[(i,a-coins[i])]
            dictt[(i,a)] = min(x, 1 + y)
            return dictt[(i,a)]
        ans = cC(0,amount) 
        if ans == math.inf:
            return -1 
        return ans
        
        
                

                
            

        

        