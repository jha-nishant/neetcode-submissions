class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        zero_count = 0
        product = 1
        for num in nums:
            if num == 0:
                zero_count = zero_count + 1
                continue
            else:
                product = product * num
        
        out = []
        for num in nums:
            if zero_count > 1:
                out.append(0)
                continue
            
            if num == 0:
                out.append(product)
            else:
                if zero_count == 1:
                    out.append(0)
                else:
                    out.append(int(product / num))
        
        return out