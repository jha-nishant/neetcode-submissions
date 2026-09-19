class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        out = []
        for i in range(len(nums) - 2):
            i_num = nums[i]
            # Need to skip current if it is same number as we will get duplicate
            if i > 0:
                if nums[i - 1] == i_num:
                    continue
            j = i + 1
            k = len(nums) - 1
            while j < k:
                # Need to skip current if it is same number as we will get duplicate.
                # We will also have to more forward due to while
                if j > i + 1:
                     if nums[j - 1] == nums[j]:
                        j = j + 1
                        continue
                j_num = nums[j]
                k_num = nums[k]
                sum = i_num + j_num + k_num 
                if sum == 0:
                    out.append([i_num, j_num, k_num])
                    j = j + 1
                elif sum > 0:
                    k = k - 1
                else:
                    j = j + 1
        return out