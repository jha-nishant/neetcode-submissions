class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        return self.singleNumberNoSpace(nums)

    def singleNumberNoSpace(self, nums: List[int]) -> int:
        result = 0
        for num in nums:
            result = result ^ num
        return result


    def singleNumberSet(self, nums: List[int]) -> int:
        num_set = set()
        for num in nums:
            if num in num_set:
                num_set.remove(num)
            else:
                num_set.add(num)
        single_num = num_set.pop()
        return single_num
