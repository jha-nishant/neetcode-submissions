class Solution:
    def jump(self, nums: List[int]) -> int:
        # store the jump required at every step
        jumps = [0]
        for i in range(1, len(nums)):
            lst = []
            for j in range(i):
                if j + nums[j] >= i:
                    hops = jumps[j] + 1
                    lst.append(hops)
            if len(jumps) == 0:
                break
            jumps.append(min(lst))
        
        if len(jumps) < len(nums):
            # Not possible what to return
            return None
        
        return jumps[len(nums) - 1]

    ## try an approach from the back how can we reach last from last -1 and so on