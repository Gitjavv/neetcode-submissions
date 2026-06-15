class Solution:
    def maxArea(self, heights: List[int]) -> int:
        max_area = 0
        l = 0
        r = len(heights) - 1
        while l < r:
            height = min(heights[l], heights[r])
            width = r-l
            area = width * height
            max_area = max(area, max_area)
            if heights[l] > heights[r]:
                r -= 1
            else:
                l += 1
        
        return max_area

    
        