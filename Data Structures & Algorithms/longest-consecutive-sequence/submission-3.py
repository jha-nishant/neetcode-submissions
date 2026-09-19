class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # First solution is n square, we need to look at all possible options
        # Second sort and trace nlogn
        # 3rd put all numbers in the set

        numbers = set(nums)
        max_length = 0

        for num in nums:
            if (num - 1) not in numbers:
                current_length = 0
                val = num
                while val in numbers:
                    current_length = current_length + 1
                    val = val + 1
                    max_length = max(current_length, max_length)
            
        return max_length
            


        