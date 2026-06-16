class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result = []
        n = len(nums)
        nums.sort()


        for i, target in enumerate(nums):
            if target > 0:
                break

            if i > 0 and target == nums[i-1]:
                continue
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
                    result.append(triplet)
                    l += 1
                    r -= 1

                    while l<r and nums[l] == nums[l-1]:
                        l+=1

                    while l<r and nums[r] == nums[r+1]:
                        r-=1
                    

        
        
        
        return result




        