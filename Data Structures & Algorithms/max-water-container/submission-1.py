class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l = 0
        r = len(heights) - 1
        max_amount = 0

        while l < r:
            bar_left = heights[l]
            bar_right = heights[r]
            if bar_left <= bar_right:
                amount = (r - l) * bar_left
                l += 1
            else:
                amount = (r - l) * bar_right
                r -= 1
            
            max_amount = max(amount, max_amount)
        
        return max_amount
            


