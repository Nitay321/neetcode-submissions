class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        buy = prices[0]
        
        for price in prices[1:]:
            profit = price - buy
            if profit > max_profit:
                max_profit = profit
            if buy > price:
                buy = price
        print(buy)
        return max_profit


    
        