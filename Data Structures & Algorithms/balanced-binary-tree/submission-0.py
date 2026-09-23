# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def __init__(self) -> None:
        self.balanced = True

    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return self.balanced
        self.depth(root)
        return self.balanced

    def depth(self, root: Optional[TreeNode]) -> int:
        left_depth, right_depth = 0, 0
        if root.left:
            left_depth = self.depth(root.left)
        if root.right:
            right_depth = self.depth(root.right)
        
        if abs(right_depth - left_depth) > 1:
            self.balanced = False
        return max(left_depth, right_depth) + 1
        