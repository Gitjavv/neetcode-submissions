class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0

        for i in range(len(prices)):
            sell = max(prices[i:])
            potential_profit = sell - prices[i]
            max_profit = max(max_profit, potential_profit)
            
        return max_profit
                