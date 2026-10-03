import math
class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        memo = [-1]*(len(cost)+1)
        cost.append(0)

        def findCost(i):
            if i == 0:
                memo[0] = cost[0]
                return cost[0]
            elif i == 1:
                memo[1] = cost[1]
                return cost[1]
            else:
                a = findCost(i-1) if memo[i-1] == -1 else memo[i-1]
                b = findCost(i-2) if memo[i-2] == -1 else memo[i-2]
                memo[i] = min(a,b) + cost[i]
                return memo[i]
        return findCost(len(cost)-1)
        



            



        