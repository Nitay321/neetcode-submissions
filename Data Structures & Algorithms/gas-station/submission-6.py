import math

class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        sumD = 0
        sumG = 0
        sumC = 0
        index = 0
        for i in range(len(gas)):
            sumG += gas[i]
            sumC += cost[i]
            sumD += gas[i]-cost[i]  
            if sumD < 0:
                index = (i + 1) % len(gas)
                sumD = 0
        
        if sumG - sumC < 0:
            return -1
        return index
        


          

           
            
      

        
        


   
        