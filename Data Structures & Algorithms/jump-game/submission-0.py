class Solution:
    def canJump(self, nums: List[int]) -> bool:
        length = len(nums)
        max_jump_index = 0
        for i in range(length):
            if i <= max_jump_index:
                num = nums[i]
                current_max_jump = i + num
                max_jump_index = max(max_jump_index, current_max_jump)
                if current_max_jump >= length - 1:
                    break
            else:
                break
        return max_jump_index >= length - 1

            
