class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        """
        Given an. integer array nums, return True if any value appears at least twice in the array,
        and return false if every element is distinct.
        """
        return len(nums) != len(set(nums))