class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        l = 0
        r = 1

        while r < len(prices):
            profit = prices[r] - prices[l]
            max_profit = max(profit, max_profit)
            r += 1
            if prices[r - 1] < prices[l]:
                l = r - 1
            
        
        return max_profit


        