class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        ## 1: n square
        ## 2: sort then iterate
        ## 3: set and compare
        ## 4: update the index with value and hasIndexValue

        slow, fast = 0, 0
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                break

        slow2 = 0
        while True:
            slow = nums[slow]
            slow2 = nums[slow2]
            if slow == slow2:
                return slow
        