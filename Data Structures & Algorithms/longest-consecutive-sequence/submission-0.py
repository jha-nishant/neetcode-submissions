class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numbers = set(nums)
        arr = []
        for num in nums:
            prev_num = num - 1
            if prev_num not in numbers:
                arr.append(num)
        
        max_length = 0

        for num in arr:
            current_length = 0
            val = num
            while val in numbers:
                current_length = current_length + 1
                val = val + 1
            if current_length > max_length:
                max_length = current_length
            
        return max_length
            


        