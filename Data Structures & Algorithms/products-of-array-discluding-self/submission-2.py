class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        return self.productExceptSelfWithoutDivision(nums)
    def productExceptSelfWithoutDivision(self, nums: List[int]) -> List[int]:
        prefix_prod = []
        suffix_prod = []

        for index, value in enumerate(nums):
            suffix_prod.append(0)
            if index == 0:
                prefix_prod.append(value)
            else:
                prod = prefix_prod[index - 1] * value
                prefix_prod.append(prod)

        for index in range(len(nums) - 1, -1, -1):
            value = nums[index]
            if index == len(nums) - 1:
                suffix_prod[index] = value
            else:
                prod = suffix_prod[index + 1] * value
                suffix_prod[index] = prod
        
        out = []
        for index, value in enumerate(nums):
            # prefix
            prefix_val = 1
            if index != 0:
                prefix_val = prefix_prod[index - 1]
            
            suffix_val = 1
            if index != len(nums) - 1:
                suffix_val = suffix_prod[index + 1]
            
            out.append(prefix_val * suffix_val)

        return out        


    
    def productExceptSelfWithDivision(self, nums: List[int]) -> List[int]:
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