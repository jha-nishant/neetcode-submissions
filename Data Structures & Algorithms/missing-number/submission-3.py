class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        return self.missingNumberBitwise(nums)

    def missingNumberBitwise(self, nums: List[int]) -> int:
        xor = len(nums)
        for index, num in enumerate(nums):
            xor ^= num ^ index
        return xor

    def missingNumberNotBitwise(self, nums: List[int]) -> int:
        sum = 0
        for num in nums:
            sum += num
        
        total = int(num * (num + 1) / 2) # division changes type to float
        return total - sum