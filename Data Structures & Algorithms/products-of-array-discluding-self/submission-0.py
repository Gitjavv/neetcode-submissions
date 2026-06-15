class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        left = [1] * len(nums)
        prod = 1
        n = len(nums)
        for i in range(1, n):
            prod *= nums[i-1]
            left[i] = prod
        
        prod2 = 1
        out = [1] * n
        out[n-1] = left[n-1]
        for j in range(n-2, -1, -1):
            prod2 *= nums[j+1]
            out[j] = left[j] * prod2

        return out