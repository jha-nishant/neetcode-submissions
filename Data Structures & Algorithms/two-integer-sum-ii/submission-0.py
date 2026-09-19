class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left = 0
        right = len(numbers) - 1

        out = []
        while right > left:
            left_num = numbers[left]
            right_num = numbers[right]

            sum = left_num + right_num

            if target == sum:
                out.append(left + 1)
                out.append(right + 1)
                break
            elif target > sum:
                left = left + 1
            else:
                right = right - 1

        return out   