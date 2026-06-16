class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result = []
        n = len(nums)
        nums.sort()


        for i, target in enumerate(nums):
            l = i + 1
            r = n - 1
            while l < r:
                suma = nums[l] + nums[r]
                if suma > -target:
                    r -= 1
                elif suma < - target:
                    l += 1
                else:
                    triplet = [target, nums[l], nums[r]]
                    if triplet not in result:
                        result.append(triplet)
                    l += 1
        
        
        
        return result




        