class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left, right = 0, len(heights) - 1
        max_area = 0
        while right > left:
            left_val, right_val = heights[left], heights[right]
            current_area = min(left_val, right_val) * (right - left)
            max_area = max(current_area, max_area)
            if left_val > right_val:
                right -= 1
            else:
                left += 1
        
        return max_area

