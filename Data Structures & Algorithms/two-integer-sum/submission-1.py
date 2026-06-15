class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        complementos = {}

        for i, elemento in enumerate(nums):
            complemento = target - elemento
            if complemento in complementos:
                return [complementos[complemento], i]
            
            complementos[elemento] = i

