import math
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        return self.maxSubArrayWithoutArray(nums)
    
    def maxSubArrayWithoutArray(self, nums: List[int]) -> int:
        max_sum = -math.inf
        current_max = -math.inf
        for index, num in enumerate(nums):
            if index == 0:
                max_sum = num
                current_max = num
            else:
                higher = max(current_max + num, num)
                current_max = higher
                max_sum = max(current_max, max_sum)
        return max_sum
    
    def maxSubArrayWithArray(self, nums: List[int]) -> int:
        max_sum = []
        for index, num in enumerate(nums):
            if index == 0:
                max_sum.append(num)
            else:
                higher = max(max_sum[index - 1] + num, num)
                max_sum.append(higher)
        
        return max(max_sum)