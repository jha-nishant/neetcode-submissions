class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        unique_numbers = set(nums)
        return len(nums) != len(unique_numbers)

        