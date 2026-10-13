class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        first = cost[0]
        second = cost[1]

        cost.append(0)

        for i in range(2,len(cost)):
            print(i, second)
            tmp = second
            second = cost[i] + min(first,second)
            first = tmp

        return second
        