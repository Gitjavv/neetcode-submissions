class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result = []
        nums.sort()
        length = len(nums)
        for i, n in enumerate(nums):
            l = i + 1
            r = length - 1
            compl = - n
            while l < r:
                suma = nums[l] + nums[r]
                if suma > compl:
                    r -= 1
                elif suma < compl:
                    l += 1
                else:
                    trio = [n, nums[l], nums[r]]
                    if trio not in result:
                        result.append(trio)
                    l += 1
        
        return result

        