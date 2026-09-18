class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        left = -1
        right = -1
        max = 0
        for index, value in enumerate(nums):
            if value == 1:
                right = index
            else:
                current = right - left
                if current > max:
                    max = current
                left = index

        current = right - left
        if current > max:
            max = current

        return max
