class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_sum = []
        for index, num in enumerate(nums):
            if index == 0:
                max_sum.append(num)
            else:
                higher = max(max_sum[index - 1] + num, num)
                max_sum.append(higher)
        
        return max(max_sum)
        