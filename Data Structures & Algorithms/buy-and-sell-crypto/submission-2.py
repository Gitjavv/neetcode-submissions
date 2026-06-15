class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0

        for i in range(len(prices)):
            for j in range(i, len(prices)):
                potential_profit = prices[j] - prices[i]
                max_profit = max(potential_profit, max_profit)
            
        return max_profit