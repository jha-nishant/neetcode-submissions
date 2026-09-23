# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def __init__(self):
        self.max_dia = 0

    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        self.maxDiameterOfBinaryTree(root)
        return self.max_dia
    
    def maxDiameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        left_depth = 0
        right_depth = 0
        if root.left:
            left_depth = self.maxDiameterOfBinaryTree(root.left)
        if root.right:
            right_depth = self.maxDiameterOfBinaryTree(root.right)

        max_dia = left_depth + right_depth
        self.max_dia = max(self.max_dia, max_dia)
        
        # max depth is going to be + 1 of max
        return max(left_depth, right_depth) + 1