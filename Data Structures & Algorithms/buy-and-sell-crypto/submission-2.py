class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy = 0
        max_profit = 0
        for i in range(len(prices)):
            profit = prices[i] - prices[buy]
            max_profit = max(profit, max_profit)

            if prices[i] < prices[buy]:
                buy = i
        
        return max_profit

        