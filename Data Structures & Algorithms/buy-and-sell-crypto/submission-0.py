class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        left_min = 101
        max_profit = 0

        for i in prices:
            left_min = min(left_min, i)
            profit = i - left_min
            max_profit = max(max_profit, profit)
        
        return max_profit
        