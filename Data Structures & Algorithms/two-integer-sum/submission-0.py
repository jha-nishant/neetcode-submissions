class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        numbers_dict = {}
        out = []
        for index, value in enumerate(nums):
            other_number = target - value
            index_other_number = numbers_dict.get(other_number)
            if index_other_number != None:
                out = [index, index_other_number]
                out.sort()
                break
            else:
                if not numbers_dict.get(value):
                    numbers_dict[value] = index
        return out